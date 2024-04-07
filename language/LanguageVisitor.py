# Generated from Language.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .LanguageParser import LanguageParser
else:
    from LanguageParser import LanguageParser

# This class defines a complete generic visitor for a parse tree produced by LanguageParser.

class LanguageVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LanguageParser#program.
    def visitProgram(self, ctx:LanguageParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#statement.
    def visitStatement(self, ctx:LanguageParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#declaration.
    def visitDeclaration(self, ctx:LanguageParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#read_statement.
    def visitRead_statement(self, ctx:LanguageParser.Read_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#write_statement.
    def visitWrite_statement(self, ctx:LanguageParser.Write_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#block.
    def visitBlock(self, ctx:LanguageParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#conditional.
    def visitConditional(self, ctx:LanguageParser.ConditionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#while_loop.
    def visitWhile_loop(self, ctx:LanguageParser.While_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#mulDivMod.
    def visitMulDivMod(self, ctx:LanguageParser.MulDivModContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#logicalNot.
    def visitLogicalNot(self, ctx:LanguageParser.LogicalNotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#equalNotEqual.
    def visitEqualNotEqual(self, ctx:LanguageParser.EqualNotEqualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#addSubConcat.
    def visitAddSubConcat(self, ctx:LanguageParser.AddSubConcatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#assignment.
    def visitAssignment(self, ctx:LanguageParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#intLiteral.
    def visitIntLiteral(self, ctx:LanguageParser.IntLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#parantheses.
    def visitParantheses(self, ctx:LanguageParser.ParanthesesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#lesserGreater.
    def visitLesserGreater(self, ctx:LanguageParser.LesserGreaterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#logicalAnd.
    def visitLogicalAnd(self, ctx:LanguageParser.LogicalAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#boolLiteral.
    def visitBoolLiteral(self, ctx:LanguageParser.BoolLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#stringLiteral.
    def visitStringLiteral(self, ctx:LanguageParser.StringLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#unaryMinus.
    def visitUnaryMinus(self, ctx:LanguageParser.UnaryMinusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#floatLiteral.
    def visitFloatLiteral(self, ctx:LanguageParser.FloatLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#id.
    def visitId(self, ctx:LanguageParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#logicalOr.
    def visitLogicalOr(self, ctx:LanguageParser.LogicalOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#type_keyword.
    def visitType_keyword(self, ctx:LanguageParser.Type_keywordContext):
        return self.visitChildren(ctx)



del LanguageParser