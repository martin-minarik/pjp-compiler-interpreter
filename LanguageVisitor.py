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


    # Visit a parse tree produced by LanguageParser#expression.
    def visitExpression(self, ctx:LanguageParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#identifier.
    def visitIdentifier(self, ctx:LanguageParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#assignment.
    def visitAssignment(self, ctx:LanguageParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#literal.
    def visitLiteral(self, ctx:LanguageParser.LiteralContext):
        return self.visitChildren(ctx)



del LanguageParser