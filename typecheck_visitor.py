from typing import Any

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

    def visitIntLiteral(self, ctx: LanguageParser.IntLiteralContext):
        return Type.Int, int(ctx.INT_LITERAL().getText())

    def visitFloatLiteral(self, ctx: LanguageParser.FloatLiteralContext):
        return Type.Float, float(ctx.FLOAT_LITERAL().getText())

    def visitBoolLiteral(self, ctx: LanguageParser.BoolLiteralContext):
        return Type.Bool, ctx.BOOL_LITERAL().getText() == "true"

    def visitStringLiteral(self, ctx: LanguageParser.StringLiteralContext):
        return Type.String, ctx.STRING_LITERAL().getText()[1:-1]

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

    def visitDeclaration(self, ctx: LanguageParser.DeclarationContext):
        type_ = self.visit(ctx.type_keyword())
        for identifier in ctx.IDENTIFIER():
            identifier: TerminalNodeImpl
            self.symbol_table.add(
                identifier.symbol, type_
            )  # Assuming add method takes IToken and Type
        return Type.Error, 0

    def visitParentheses(self, ctx: LanguageParser.ParenthesesContext):
        return self.visit(ctx.expression())

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
