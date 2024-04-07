# Generated from Language.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .LanguageParser import LanguageParser
else:
    from LanguageParser import LanguageParser

# This class defines a complete listener for a parse tree produced by LanguageParser.
class LanguageListener(ParseTreeListener):

    # Enter a parse tree produced by LanguageParser#program.
    def enterProgram(self, ctx:LanguageParser.ProgramContext):
        pass

    # Exit a parse tree produced by LanguageParser#program.
    def exitProgram(self, ctx:LanguageParser.ProgramContext):
        pass


    # Enter a parse tree produced by LanguageParser#statement.
    def enterStatement(self, ctx:LanguageParser.StatementContext):
        pass

    # Exit a parse tree produced by LanguageParser#statement.
    def exitStatement(self, ctx:LanguageParser.StatementContext):
        pass


    # Enter a parse tree produced by LanguageParser#declaration.
    def enterDeclaration(self, ctx:LanguageParser.DeclarationContext):
        pass

    # Exit a parse tree produced by LanguageParser#declaration.
    def exitDeclaration(self, ctx:LanguageParser.DeclarationContext):
        pass


    # Enter a parse tree produced by LanguageParser#read_statement.
    def enterRead_statement(self, ctx:LanguageParser.Read_statementContext):
        pass

    # Exit a parse tree produced by LanguageParser#read_statement.
    def exitRead_statement(self, ctx:LanguageParser.Read_statementContext):
        pass


    # Enter a parse tree produced by LanguageParser#write_statement.
    def enterWrite_statement(self, ctx:LanguageParser.Write_statementContext):
        pass

    # Exit a parse tree produced by LanguageParser#write_statement.
    def exitWrite_statement(self, ctx:LanguageParser.Write_statementContext):
        pass


    # Enter a parse tree produced by LanguageParser#block.
    def enterBlock(self, ctx:LanguageParser.BlockContext):
        pass

    # Exit a parse tree produced by LanguageParser#block.
    def exitBlock(self, ctx:LanguageParser.BlockContext):
        pass


    # Enter a parse tree produced by LanguageParser#conditional.
    def enterConditional(self, ctx:LanguageParser.ConditionalContext):
        pass

    # Exit a parse tree produced by LanguageParser#conditional.
    def exitConditional(self, ctx:LanguageParser.ConditionalContext):
        pass


    # Enter a parse tree produced by LanguageParser#while_loop.
    def enterWhile_loop(self, ctx:LanguageParser.While_loopContext):
        pass

    # Exit a parse tree produced by LanguageParser#while_loop.
    def exitWhile_loop(self, ctx:LanguageParser.While_loopContext):
        pass


    # Enter a parse tree produced by LanguageParser#expression.
    def enterExpression(self, ctx:LanguageParser.ExpressionContext):
        pass

    # Exit a parse tree produced by LanguageParser#expression.
    def exitExpression(self, ctx:LanguageParser.ExpressionContext):
        pass


    # Enter a parse tree produced by LanguageParser#assignment.
    def enterAssignment(self, ctx:LanguageParser.AssignmentContext):
        pass

    # Exit a parse tree produced by LanguageParser#assignment.
    def exitAssignment(self, ctx:LanguageParser.AssignmentContext):
        pass


    # Enter a parse tree produced by LanguageParser#type_keyword.
    def enterType_keyword(self, ctx:LanguageParser.Type_keywordContext):
        pass

    # Exit a parse tree produced by LanguageParser#type_keyword.
    def exitType_keyword(self, ctx:LanguageParser.Type_keywordContext):
        pass


    # Enter a parse tree produced by LanguageParser#int.
    def enterInt(self, ctx:LanguageParser.IntContext):
        pass

    # Exit a parse tree produced by LanguageParser#int.
    def exitInt(self, ctx:LanguageParser.IntContext):
        pass


    # Enter a parse tree produced by LanguageParser#float.
    def enterFloat(self, ctx:LanguageParser.FloatContext):
        pass

    # Exit a parse tree produced by LanguageParser#float.
    def exitFloat(self, ctx:LanguageParser.FloatContext):
        pass


    # Enter a parse tree produced by LanguageParser#bool.
    def enterBool(self, ctx:LanguageParser.BoolContext):
        pass

    # Exit a parse tree produced by LanguageParser#bool.
    def exitBool(self, ctx:LanguageParser.BoolContext):
        pass


    # Enter a parse tree produced by LanguageParser#string.
    def enterString(self, ctx:LanguageParser.StringContext):
        pass

    # Exit a parse tree produced by LanguageParser#string.
    def exitString(self, ctx:LanguageParser.StringContext):
        pass



del LanguageParser