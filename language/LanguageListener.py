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


    # Enter a parse tree produced by LanguageParser#mulDivMod.
    def enterMulDivMod(self, ctx:LanguageParser.MulDivModContext):
        pass

    # Exit a parse tree produced by LanguageParser#mulDivMod.
    def exitMulDivMod(self, ctx:LanguageParser.MulDivModContext):
        pass


    # Enter a parse tree produced by LanguageParser#logicalNot.
    def enterLogicalNot(self, ctx:LanguageParser.LogicalNotContext):
        pass

    # Exit a parse tree produced by LanguageParser#logicalNot.
    def exitLogicalNot(self, ctx:LanguageParser.LogicalNotContext):
        pass


    # Enter a parse tree produced by LanguageParser#equalNotEqual.
    def enterEqualNotEqual(self, ctx:LanguageParser.EqualNotEqualContext):
        pass

    # Exit a parse tree produced by LanguageParser#equalNotEqual.
    def exitEqualNotEqual(self, ctx:LanguageParser.EqualNotEqualContext):
        pass


    # Enter a parse tree produced by LanguageParser#addSubConcat.
    def enterAddSubConcat(self, ctx:LanguageParser.AddSubConcatContext):
        pass

    # Exit a parse tree produced by LanguageParser#addSubConcat.
    def exitAddSubConcat(self, ctx:LanguageParser.AddSubConcatContext):
        pass


    # Enter a parse tree produced by LanguageParser#assignment.
    def enterAssignment(self, ctx:LanguageParser.AssignmentContext):
        pass

    # Exit a parse tree produced by LanguageParser#assignment.
    def exitAssignment(self, ctx:LanguageParser.AssignmentContext):
        pass


    # Enter a parse tree produced by LanguageParser#intLiteral.
    def enterIntLiteral(self, ctx:LanguageParser.IntLiteralContext):
        pass

    # Exit a parse tree produced by LanguageParser#intLiteral.
    def exitIntLiteral(self, ctx:LanguageParser.IntLiteralContext):
        pass


    # Enter a parse tree produced by LanguageParser#parantheses.
    def enterParantheses(self, ctx:LanguageParser.ParanthesesContext):
        pass

    # Exit a parse tree produced by LanguageParser#parantheses.
    def exitParantheses(self, ctx:LanguageParser.ParanthesesContext):
        pass


    # Enter a parse tree produced by LanguageParser#lesserGreater.
    def enterLesserGreater(self, ctx:LanguageParser.LesserGreaterContext):
        pass

    # Exit a parse tree produced by LanguageParser#lesserGreater.
    def exitLesserGreater(self, ctx:LanguageParser.LesserGreaterContext):
        pass


    # Enter a parse tree produced by LanguageParser#logicalAnd.
    def enterLogicalAnd(self, ctx:LanguageParser.LogicalAndContext):
        pass

    # Exit a parse tree produced by LanguageParser#logicalAnd.
    def exitLogicalAnd(self, ctx:LanguageParser.LogicalAndContext):
        pass


    # Enter a parse tree produced by LanguageParser#boolLiteral.
    def enterBoolLiteral(self, ctx:LanguageParser.BoolLiteralContext):
        pass

    # Exit a parse tree produced by LanguageParser#boolLiteral.
    def exitBoolLiteral(self, ctx:LanguageParser.BoolLiteralContext):
        pass


    # Enter a parse tree produced by LanguageParser#stringLiteral.
    def enterStringLiteral(self, ctx:LanguageParser.StringLiteralContext):
        pass

    # Exit a parse tree produced by LanguageParser#stringLiteral.
    def exitStringLiteral(self, ctx:LanguageParser.StringLiteralContext):
        pass


    # Enter a parse tree produced by LanguageParser#unaryMinus.
    def enterUnaryMinus(self, ctx:LanguageParser.UnaryMinusContext):
        pass

    # Exit a parse tree produced by LanguageParser#unaryMinus.
    def exitUnaryMinus(self, ctx:LanguageParser.UnaryMinusContext):
        pass


    # Enter a parse tree produced by LanguageParser#floatLiteral.
    def enterFloatLiteral(self, ctx:LanguageParser.FloatLiteralContext):
        pass

    # Exit a parse tree produced by LanguageParser#floatLiteral.
    def exitFloatLiteral(self, ctx:LanguageParser.FloatLiteralContext):
        pass


    # Enter a parse tree produced by LanguageParser#id.
    def enterId(self, ctx:LanguageParser.IdContext):
        pass

    # Exit a parse tree produced by LanguageParser#id.
    def exitId(self, ctx:LanguageParser.IdContext):
        pass


    # Enter a parse tree produced by LanguageParser#logicalOr.
    def enterLogicalOr(self, ctx:LanguageParser.LogicalOrContext):
        pass

    # Exit a parse tree produced by LanguageParser#logicalOr.
    def exitLogicalOr(self, ctx:LanguageParser.LogicalOrContext):
        pass


    # Enter a parse tree produced by LanguageParser#type_keyword.
    def enterType_keyword(self, ctx:LanguageParser.Type_keywordContext):
        pass

    # Exit a parse tree produced by LanguageParser#type_keyword.
    def exitType_keyword(self, ctx:LanguageParser.Type_keywordContext):
        pass



del LanguageParser