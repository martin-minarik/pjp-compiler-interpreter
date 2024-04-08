from antlr4.tree.Tree import TerminalNodeImpl

from errors import Errors
from language.LanguageParser import LanguageParser
from language.LanguageVisitor import LanguageVisitor
from symbol_table import SymbolTable
from type_enum import Type


class TypeCheckingVisitor(LanguageVisitor):
    def __init__(self):
        self.symbol_table = SymbolTable()
        self.binary_operations_table: dict[tuple[Type, Type, int], Type] = {
            (Type.Int, Type.Int, LanguageParser.MUL): Type.Int,
            (Type.Float, Type.Float, LanguageParser.MUL): Type.Float,
            (Type.Int, Type.Int, LanguageParser.DIV): Type.Int,
            (Type.Float, Type.Float, LanguageParser.DIV): Type.Float,
            (Type.Int, Type.Int, LanguageParser.MOD): Type.Int,
            (Type.Int, Type.Int, LanguageParser.ADD): Type.Int,
            (Type.Float, Type.Float, LanguageParser.ADD): Type.Float,
            (Type.Int, Type.Int, LanguageParser.SUB): Type.Int,
            (Type.Float, Type.Float, LanguageParser.SUB): Type.Float,
            (Type.String, Type.String, LanguageParser.CONCAT): Type.String,
        }

    def visitType_keyword(self, ctx: LanguageParser.Type_keywordContext):
        match ctx.getText():
            case "float":
                return Type.Float
            case "int":
                return Type.Int
            case "string":
                return Type.String
            case "bool":
                return Type.Bool

    @staticmethod
    def resolve_left_right_types(type_a: Type, type_b: Type) -> tuple[Type, Type]:
        if TypeCheckingVisitor.check_float_cast(type_a, type_b):
            return Type.Float, Type.Float

        return type_a, type_b

    @staticmethod
    def check_float_cast(type_a: Type, type_b: Type) -> bool:
        if (type_a == Type.Int) or (type_b == Type.Int):
            if (type_a == Type.Float) or (type_b == Type.Float):
                return True

        return False

    def visitConditional(self, ctx: LanguageParser.ConditionalContext):
        condition = self.visit(ctx.condition)
        if condition != Type.Bool:
            Errors.report_error_rule_context(
                ctx.condition,
                f"Invalid condition. Should an expression with a type bool!",
            )

        self.visitChildren(ctx)

        return Type.Error

    def visitWhile_loop(self, ctx: LanguageParser.While_loopContext):
        condition = self.visit(ctx.condition)
        if condition != Type.Bool:
            Errors.report_error_rule_context(
                ctx.condition,
                f"Invalid condition. Should an expression with a type bool!",
            )

        self.visitChildren(ctx)

        return Type.Error

    def visitFor_loop(self, ctx:LanguageParser.For_loopContext):
        self.visit(ctx.expression()[0])
        condition = self.visit(ctx.expression()[1])
        self.visit(ctx.expression()[2])

        if condition != Type.Bool:
            Errors.report_error_rule_context(
                ctx.expression()[1],
                f"Invalid condition. Should an expression with a type bool!",
            )


    def visitIntLiteral(self, ctx: LanguageParser.IntLiteralContext):
        return Type.Int

    def visitFloatLiteral(self, ctx: LanguageParser.FloatLiteralContext):
        return Type.Float

    def visitBoolLiteral(self, ctx: LanguageParser.BoolLiteralContext):
        return Type.Bool

    def visitStringLiteral(self, ctx: LanguageParser.StringLiteralContext):
        return Type.String

    def visitLogicalNot(self, ctx: LanguageParser.LogicalNotContext):
        variable = self.visit(ctx.expression())
        if variable == Type.Bool:
            return Type.Bool

        Errors.report_error(
            ctx.prefix,
            f"Invalid type for logical negation!",
        )

        return Type.Error

    def visitUnaryMinus(self, ctx: LanguageParser.UnaryMinusContext):
        variable = self.visit(ctx.expression())
        if variable in (Type.Int, Type.Float):
            return variable

        Errors.report_error(
            ctx.prefix,
            f"Invalid type for unary minus!",
        )

        return Type.Error

    def visitMulDivMod(self, ctx: LanguageParser.MulDivModContext):
        left = self.visit(ctx.expression()[0])
        right = self.visit(ctx.expression()[1])

        type_left, type_right = self.resolve_left_right_types(left, right)
        if type_ := self.binary_operations_table.get(
                (type_left, type_right, ctx.op.type)
        ):
            return type_

        Errors.report_error(ctx.op, f"Invalid operation. \"{left.name} {ctx.op.text} {right.name}\"")

        return Type.Error

    def visitAddSubConcat(self, ctx: LanguageParser.AddSubConcatContext):
        left = self.visit(ctx.expression()[0])
        right = self.visit(ctx.expression()[1])

        if (left == Type.Error) or (right == Type.Error):
            return Type.Error

        type_left, type_right = self.resolve_left_right_types(left, right)
        if type_ := self.binary_operations_table.get(
                (type_left, type_right, ctx.op.type)
        ):
            return type_

        Errors.report_error(ctx.op, f"Invalid operation. \"{left.name} {ctx.op.text} {right.name}\"")

        return Type.Error

    def visitLesserGreater(self, ctx: LanguageParser.LesserGreaterContext):
        left = self.visit(ctx.expression()[0])
        right = self.visit(ctx.expression()[1])
        if (left == Type.Error) or (right == Type.Error):
            return Type.Error

        if (left in (Type.Int, Type.Float)) and (right in (Type.Int, Type.Float)):
            return Type.Bool

        Errors.report_error(
            ctx.op,
            f"Invalid type for comparison!",
        )

        return Type.Error

    def visitEqualNotEqual(self, ctx: LanguageParser.EqualNotEqualContext):
        left = self.visit(ctx.expression()[0])
        right = self.visit(ctx.expression()[1])

        left_type, right_type = self.resolve_left_right_types(left, right)
        if left_type == right_type:
            return Type.Bool

        Errors.report_error(
            ctx.op,
            f"Invalid type for equality testing!",
        )

        return Type.Error

    def visitLogicalAnd(self, ctx: LanguageParser.LogicalAndContext):
        left = self.visit(ctx.expression()[0])
        right = self.visit(ctx.expression()[1])
        if (left == Type.Error) or (right == Type.Error):
            return Type.Error

        if (left == Type.Bool) and (right == Type.Bool):
            return Type.Bool

        Errors.report_error(
            ctx.op,
            f"Invalid type for logical AND!",
        )

        return Type.Error

    def visitLogicalOr(self, ctx: LanguageParser.LogicalAndContext):
        left = self.visit(ctx.expression()[0])
        right = self.visit(ctx.expression()[1])
        if (left == Type.Error) or (right == Type.Error):
            return Type.Error

        if (left == Type.Bool) and (right == Type.Bool):
            return Type.Bool

        Errors.report_error(
            ctx.op,
            f"Invalid type for logical OR!",
        )

        return Type.Error

    def visitDeclaration(self, ctx: LanguageParser.DeclarationContext):
        type_ = self.visit(ctx.type_keyword())
        for identifier in ctx.IDENTIFIER():
            identifier: TerminalNodeImpl
            self.symbol_table.add(identifier.symbol, type_)
        return Type.Error

    def visitParentheses(self, ctx: LanguageParser.ParenthesesContext):
        return self.visit(ctx.expression())

    def visitId(self, ctx: LanguageParser.IdContext):
        return self.symbol_table[ctx.IDENTIFIER().symbol]

    def visitAssignment(self, ctx: LanguageParser.AssignmentContext):
        variable = self.symbol_table[ctx.IDENTIFIER().symbol]
        right = self.visit(ctx.expression())

        if (variable == Type.Error) or (right == Type.Error):
            return Type.Error

        if (variable == Type.Int) and (right == Type.Float):
            Errors.report_error(
                ctx.IDENTIFIER().symbol,
                f"Variable '{ctx.IDENTIFIER().getText()}' type is int, but the assigned value is float.",
            )
            return Type.Error

        if (variable == Type.Float) and (right == Type.Int):
            value = Type.Float
            self.symbol_table[ctx.IDENTIFIER().symbol] = value
            return value
        else:
            if right != self.symbol_table[ctx.IDENTIFIER().symbol]:
                Errors.report_error(
                    ctx.IDENTIFIER().symbol,
                    f"Variable '{ctx.IDENTIFIER().getText()}' type is {variable.name.lower()},"
                    f" but the assigned is {right.name.lower()}",
                )

            return right
