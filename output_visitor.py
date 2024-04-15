from antlr4.tree.Tree import TerminalNodeImpl

from language.LanguageParser import LanguageParser, ParserRuleContext
from language.LanguageVisitor import LanguageVisitor
from symbol_table import SymbolTable
from type_enum import Type


class OutputVisitor(LanguageVisitor):
    def __init__(self, symbol_table: SymbolTable, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.symbol_table = symbol_table
        self.output_list = []
        self.type_single_letter_dir: dict[Type, str] = {
            Type.Int: "I",
            Type.Float: "F",
            Type.Bool: "B",
            Type.String: "S",
        }

    def resolve_itof_binary_op(self, left: ParserRuleContext, right: ParserRuleContext):
        if isinstance(left, LanguageParser.IntLiteralContext) and isinstance(
                right, LanguageParser.FloatLiteralContext
        ):
            self.output_list.append("itof")

    def visitIntLiteral(self, ctx: LanguageParser.IntLiteralContext):
        self.output_list.append(f"push I {ctx.INT_LITERAL().getText()}")

    def visitFloatLiteral(self, ctx: LanguageParser.FloatLiteralContext):
        self.output_list.append(f"push F {ctx.FLOAT_LITERAL().getText()}")

    def visitBoolLiteral(self, ctx: LanguageParser.BoolLiteralContext):
        self.output_list.append(f"push B {ctx.BOOL_LITERAL().getText()}")

    def visitStringLiteral(self, ctx: LanguageParser.StringLiteralContext):
        self.output_list.append(f"push S {ctx.STRING_LITERAL().getText()}")

    def visitParentheses(self, ctx: LanguageParser.ParenthesesContext):
        return self.visit(ctx.expression())

    def visitWrite_statement(self, ctx: LanguageParser.Write_statementContext):
        for expression in ctx.expression():
            self.visit(expression)

        self.output_list.append(f"print {len(ctx.expression())}")

    def visitRead_statement(self, ctx: LanguageParser.Read_statementContext):
        for identifier in ctx.IDENTIFIER():
            identifier: TerminalNodeImpl
            type_single_letter = self.type_single_letter_dir[
                self.symbol_table[identifier.symbol]
            ]
            self.output_list.append(f"read {type_single_letter}")
            self.output_list.append(f"save {identifier.getText()}")

    def visitUnaryMinus(self, ctx: LanguageParser.UnaryMinusContext):
        self.visit(ctx.expression())
        self.output_list.append(f"uminus")

    def visitProgram(self, ctx: LanguageParser.ProgramContext):
        for statement in ctx.statement():
            statement: ParserRuleContext
            self.visit(statement)

        return self.output_list

    def visitType_keyword(self, ctx: LanguageParser.Type_keywordContext):
        match ctx.getText():
            case "int":
                self.output_list.append("push I 0")
            case "float":
                self.output_list.append("push F 0.0")
            case "string":
                self.output_list.append('push S ""')
            case "bool":
                self.output_list.append("push B true")

    def visitId(self, ctx: LanguageParser.IdContext):
        self.output_list.append(f"load {ctx.IDENTIFIER().getText()}")

    def visitMulDivMod(self, ctx: LanguageParser.MulDivModContext):
        left = ctx.expression()[0]
        right = ctx.expression()[1]
        self.visit(left)
        self.resolve_itof_binary_op(left, right)

        self.visit(right)
        self.resolve_itof_binary_op(right, left)

        match ctx.op.type:
            case LanguageParser.MUL:
                self.output_list.append("mul")
            case LanguageParser.DIV:
                self.output_list.append("div")
            case LanguageParser.MOD:
                self.output_list.append("mod")

    def visitAddSubConcat(self, ctx: LanguageParser.MulDivModContext):
        left = ctx.expression()[0]
        right = ctx.expression()[1]
        self.visit(left)
        self.resolve_itof_binary_op(left, right)

        self.visit(right)
        self.resolve_itof_binary_op(right, left)

        match ctx.op.type:
            case LanguageParser.ADD:
                self.output_list.append("add")
            case LanguageParser.SUB:
                self.output_list.append("sub")
            case LanguageParser.CONCAT:
                self.output_list.append("concat")

    def visitLesserGreater(self, ctx: LanguageParser.MulDivModContext):
        left = ctx.expression()[0]
        right = ctx.expression()[1]
        self.visit(left)
        self.resolve_itof_binary_op(left, right)

        self.visit(right)
        self.resolve_itof_binary_op(right, left)

        match ctx.op.type:
            case LanguageParser.LT:
                self.output_list.append("lt")
            case LanguageParser.GT:
                self.output_list.append("gt")

    def visitEqualNotEqual(self, ctx: LanguageParser.MulDivModContext):
        left = ctx.expression()[0]
        right = ctx.expression()[1]
        self.visit(left)
        self.visit(right)

        match ctx.op.type:
            case LanguageParser.EQUAL:
                self.output_list.append("eq")
            case LanguageParser.NOTEQUAL:
                self.output_list.append("eq")
                self.output_list.append("not")

    def visitLogicalAnd(self, ctx: LanguageParser.MulDivModContext):
        left = ctx.expression()[0]
        right = ctx.expression()[1]
        self.visit(left)
        self.visit(right)

        self.output_list.append("and")

    def visitLogicalOr(self, ctx: LanguageParser.MulDivModContext):
        left = ctx.expression()[0]
        right = ctx.expression()[1]
        self.visit(left)
        self.visit(right)

        self.output_list.append("or")

    def visitLogicalNot(self, ctx: LanguageParser.MulDivModContext):
        self.visit(ctx.expression())

        self.output_list.append("not")

    def visitDeclaration(self, ctx: LanguageParser.DeclarationContext):
        for identifier in ctx.IDENTIFIER():
            identifier: TerminalNodeImpl
            self.visit(ctx.type_keyword())
            self.output_list.append(f"save {identifier.getText()}")

    def visitAssignment(self, ctx: LanguageParser.AssignmentContext):
        self.visit(ctx.expression())

        # itof
        if self.symbol_table[ctx.IDENTIFIER().symbol] == Type.Float and isinstance(
                ctx.expression(), LanguageParser.IntLiteralContext
        ):
            self.output_list.append("itof")

        self.output_list.append(f"save {ctx.IDENTIFIER().getText()}")
        self.output_list.append(f"load {ctx.IDENTIFIER().getText()}")

        if not isinstance(ctx.parentCtx, LanguageParser.AssignmentContext):
            self.output_list.append(f"pop")

        return ctx.expression()
