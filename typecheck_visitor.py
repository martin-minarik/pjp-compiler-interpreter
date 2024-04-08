import operator as op
from typing import Any, Callable

from antlr4.Token import *
from antlr4.tree.Tree import TerminalNodeImpl

from errors import Errors
from language.LanguageParser import LanguageParser
from language.LanguageVisitor import LanguageVisitor
from symbol_table import SymbolTable
from type_enum import Type


class TypeCheckingVisitor(LanguageVisitor):
    def __init__(self):
        self.symbol_table = SymbolTable()
        self.binary_operations_table: dict[
            tuple[Type, Type, int], tuple[Type, Callable]
        ] = {
            (Type.Int, Type.Int, LanguageParser.MUL): (Type.Int, op.mul),
            (Type.Float, Type.Float, LanguageParser.MUL): (Type.Float, op.mul),
            (Type.Int, Type.Int, LanguageParser.DIV): (Type.Int, op.floordiv),
            (Type.Float, Type.Float, LanguageParser.DIV): (Type.Float, op.truediv),
            (Type.Int, Type.Int, LanguageParser.MOD): (Type.Int, op.imod),
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

    def visitIntLiteral(self, ctx: LanguageParser.IntLiteralContext):
        return Type.Int, int(ctx.INT_LITERAL().getText())

    def visitFloatLiteral(self, ctx: LanguageParser.FloatLiteralContext):
        return Type.Float, float(ctx.FLOAT_LITERAL().getText())

    def visitBoolLiteral(self, ctx: LanguageParser.BoolLiteralContext):
        return Type.Bool, ctx.BOOL_LITERAL().getText() == "true"

    def visitStringLiteral(self, ctx: LanguageParser.StringLiteralContext):
        return Type.String, ctx.STRING_LITERAL().getText()[1:-1]

    def visitLogicalNot(self, ctx: LanguageParser.LogicalNotContext):
        variable = self.visit(ctx.expression())
        if variable[0] == Type.Bool:
            return Type.Bool, not variable[1]

        Errors.report_error(
            ctx.op,
            f"Invalid type operation!",
        )

        return Type.Error, 0

    def visitUnaryMinus(self, ctx: LanguageParser.UnaryMinusContext):
        variable = self.visit(ctx.expression())
        if variable[0] in (Type.Int, Type.Float):
            return variable[0], -variable[1]

        Errors.report_error(
            ctx.op,
            f"Invalid type operation!",
        )

        return Type.Error, 0

    def visitMulDivMod(self, ctx: LanguageParser.MulDivModContext):
        left = self.visit(ctx.expression()[0])
        right = self.visit(ctx.expression()[1])

        type_left, type_right = self.resolve_left_right_types(left[0], right[0])
        if type_op := self.binary_operations_table.get(
            (type_left, type_right, ctx.op.type)
        ):
            return type_op[0], type_op[1](left[1], right[1])

        Errors.report_error(
            ctx.op,
            f"Invalid type operation!",
        )

        return Type.Error, 0

    def visitAddSubConcat(self, ctx: LanguageParser.AddSubConcatContext):
        left = self.visit(ctx.expression()[0])
        right = self.visit(ctx.expression()[1])

        if (left[0] == Type.Error) or (right[0] == Type.Error):
            return Type.Error, 0

        # Numeric operations
        if (left[0] in (Type.Int, Type.Float)) and (right[0] in (Type.Int, Type.Float)):
            match ctx.op.type:
                case LanguageParser.ADD:
                    result = left[1] + right[1]

                case LanguageParser.SUB:
                    result = left[1] - right[1]

                case _:
                    Errors.report_error(
                        ctx.op,
                        f"Invalid numeric operation!",
                    )
                    return Type.Error, 0

            type_ = Type.Float if isinstance(result, float) else Type.Int
            return type_, result

        # String operations
        elif (left[0] == Type.String) and (right[0] == Type.String):
            if ctx.op.type == LanguageParser.CONCAT:
                return Type.String, left[1] + right[1]

        Errors.report_error(
            ctx.op,
            f"Invalid type operation!",
        )

        return Type.Error, 0

    def visitLesserGreater(self, ctx: LanguageParser.LesserGreaterContext):
        left = self.visit(ctx.expression()[0])
        right = self.visit(ctx.expression()[1])
        if (left[0] == Type.Error) or (right[0] == Type.Error):
            return Type.Error, 0

        if (left[0] in (Type.Int, Type.Float)) and (right[0] in (Type.Int, Type.Float)):
            result = (op.gt if ctx.op.type == LanguageParser.GT else op.lt)(
                left[1], right[1]
            )
            return Type.Bool, result

        Errors.report_error(
            ctx.op,
            f"Invalid type operation!",
        )

        return Type.Error, 0

    def visitLogicalAnd(self, ctx: LanguageParser.LogicalAndContext):
        left = self.visit(ctx.expression()[0])
        right = self.visit(ctx.expression()[1])
        if (left[0] == Type.Error) or (right[0] == Type.Error):
            return Type.Error, 0

        if (left[0] == Type.Bool) and (right[0] == Type.Bool):
            return Type.Bool, left[1] and right[1]

        Errors.report_error(
            ctx.op,
            f"Invalid type operation!",
        )

        return Type.Error, 0

    def visitLogicalOr(self, ctx: LanguageParser.LogicalAndContext):
        left = self.visit(ctx.expression()[0])
        right = self.visit(ctx.expression()[1])
        if (left[0] == Type.Error) or (right[0] == Type.Error):
            return Type.Error, 0

        if (left[0] == Type.Bool) and (right[0] == Type.Bool):
            return Type.Bool, left[1] or right[1]

        Errors.report_error(
            ctx.op,
            f"Invalid type operation!",
        )

        return Type.Error, 0

    def visitDeclaration(self, ctx: LanguageParser.DeclarationContext):
        type_ = self.visit(ctx.type_keyword())
        for identifier in ctx.IDENTIFIER():
            identifier: TerminalNodeImpl
            self.symbol_table.add(identifier.symbol, type_)
        return Type.Error, 0

    def visitParentheses(self, ctx: LanguageParser.ParenthesesContext):
        return self.visit(ctx.expression())

    def visitId(self, ctx: LanguageParser.IdContext):
        return self.symbol_table[ctx.IDENTIFIER().symbol]

    def visitAssignment(self, ctx: LanguageParser.AssignmentContext):
        variable = self.symbol_table[ctx.IDENTIFIER().symbol]
        right = self.visit(ctx.expression())

        if (variable[0] == Type.Error) or (right[0] == Type.Error):
            return Type.Error, 0

        if (variable[0] == Type.Int) and (right[0] == Type.Float):
            Errors.report_error(
                ctx.IDENTIFIER().symbol,
                f"Variable '{ctx.IDENTIFIER().getText()}' type is int, but the assigned value is float.",
            )
            return Type.Error, 0

        if (variable[0] == Type.Float) and (right[0] == Type.Int):
            value = Type.Float, float(right[1])
            self.symbol_table[ctx.IDENTIFIER().symbol] = value
            return value
        else:
            self.symbol_table[ctx.IDENTIFIER().symbol] = right
            return right
