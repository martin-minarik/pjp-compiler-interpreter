# Generated from Language.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,33,143,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,4,0,24,8,0,11,0,12,0,25,
        1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,41,8,1,1,
        2,1,2,1,2,1,2,5,2,47,8,2,10,2,12,2,50,9,2,1,2,1,2,1,3,1,3,1,3,1,
        3,5,3,58,8,3,10,3,12,3,61,9,3,1,3,1,3,1,4,1,4,1,4,1,4,5,4,69,8,4,
        10,4,12,4,72,9,4,1,4,1,4,1,5,1,5,5,5,78,8,5,10,5,12,5,81,9,5,1,5,
        1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,92,8,6,1,7,1,7,1,7,1,7,1,7,1,
        7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,112,8,8,1,
        8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,
        8,1,8,5,8,132,8,8,10,8,12,8,135,9,8,1,9,1,9,1,9,1,9,1,10,1,10,1,
        10,0,1,16,11,0,2,4,6,8,10,12,14,16,18,20,0,5,2,0,28,29,32,32,2,0,
        30,31,33,33,1,0,13,14,1,0,15,16,2,0,20,22,25,25,156,0,23,1,0,0,0,
        2,40,1,0,0,0,4,42,1,0,0,0,6,53,1,0,0,0,8,64,1,0,0,0,10,75,1,0,0,
        0,12,84,1,0,0,0,14,93,1,0,0,0,16,111,1,0,0,0,18,136,1,0,0,0,20,140,
        1,0,0,0,22,24,3,2,1,0,23,22,1,0,0,0,24,25,1,0,0,0,25,23,1,0,0,0,
        25,26,1,0,0,0,26,27,1,0,0,0,27,28,5,0,0,1,28,1,1,0,0,0,29,41,5,1,
        0,0,30,41,3,4,2,0,31,32,3,16,8,0,32,33,5,1,0,0,33,41,1,0,0,0,34,
        41,3,6,3,0,35,41,3,8,4,0,36,41,3,10,5,0,37,41,3,12,6,0,38,41,3,14,
        7,0,39,41,5,24,0,0,40,29,1,0,0,0,40,30,1,0,0,0,40,31,1,0,0,0,40,
        34,1,0,0,0,40,35,1,0,0,0,40,36,1,0,0,0,40,37,1,0,0,0,40,38,1,0,0,
        0,40,39,1,0,0,0,41,3,1,0,0,0,42,43,5,26,0,0,43,48,5,27,0,0,44,45,
        5,2,0,0,45,47,5,27,0,0,46,44,1,0,0,0,47,50,1,0,0,0,48,46,1,0,0,0,
        48,49,1,0,0,0,49,51,1,0,0,0,50,48,1,0,0,0,51,52,5,1,0,0,52,5,1,0,
        0,0,53,54,5,3,0,0,54,59,5,27,0,0,55,56,5,2,0,0,56,58,5,27,0,0,57,
        55,1,0,0,0,58,61,1,0,0,0,59,57,1,0,0,0,59,60,1,0,0,0,60,62,1,0,0,
        0,61,59,1,0,0,0,62,63,5,1,0,0,63,7,1,0,0,0,64,65,5,4,0,0,65,70,3,
        16,8,0,66,67,5,2,0,0,67,69,3,16,8,0,68,66,1,0,0,0,69,72,1,0,0,0,
        70,68,1,0,0,0,70,71,1,0,0,0,71,73,1,0,0,0,72,70,1,0,0,0,73,74,5,
        1,0,0,74,9,1,0,0,0,75,79,5,5,0,0,76,78,3,2,1,0,77,76,1,0,0,0,78,
        81,1,0,0,0,79,77,1,0,0,0,79,80,1,0,0,0,80,82,1,0,0,0,81,79,1,0,0,
        0,82,83,5,6,0,0,83,11,1,0,0,0,84,85,5,7,0,0,85,86,5,8,0,0,86,87,
        3,16,8,0,87,88,5,9,0,0,88,91,3,2,1,0,89,90,5,10,0,0,90,92,3,2,1,
        0,91,89,1,0,0,0,91,92,1,0,0,0,92,13,1,0,0,0,93,94,5,11,0,0,94,95,
        5,8,0,0,95,96,3,16,8,0,96,97,5,9,0,0,97,98,3,2,1,0,98,15,1,0,0,0,
        99,100,6,8,-1,0,100,101,5,31,0,0,101,112,3,16,8,12,102,103,5,12,
        0,0,103,112,3,16,8,11,104,105,5,8,0,0,105,106,3,16,8,0,106,107,5,
        9,0,0,107,112,1,0,0,0,108,112,3,18,9,0,109,112,5,27,0,0,110,112,
        3,20,10,0,111,99,1,0,0,0,111,102,1,0,0,0,111,104,1,0,0,0,111,108,
        1,0,0,0,111,109,1,0,0,0,111,110,1,0,0,0,112,133,1,0,0,0,113,114,
        10,10,0,0,114,115,7,0,0,0,115,132,3,16,8,11,116,117,10,9,0,0,117,
        118,7,1,0,0,118,132,3,16,8,10,119,120,10,8,0,0,120,121,7,2,0,0,121,
        132,3,16,8,9,122,123,10,7,0,0,123,124,7,3,0,0,124,132,3,16,8,8,125,
        126,10,6,0,0,126,127,5,17,0,0,127,132,3,16,8,7,128,129,10,5,0,0,
        129,130,5,18,0,0,130,132,3,16,8,6,131,113,1,0,0,0,131,116,1,0,0,
        0,131,119,1,0,0,0,131,122,1,0,0,0,131,125,1,0,0,0,131,128,1,0,0,
        0,132,135,1,0,0,0,133,131,1,0,0,0,133,134,1,0,0,0,134,17,1,0,0,0,
        135,133,1,0,0,0,136,137,5,27,0,0,137,138,5,19,0,0,138,139,3,16,8,
        0,139,19,1,0,0,0,140,141,7,4,0,0,141,21,1,0,0,0,10,25,40,48,59,70,
        79,91,111,131,133
    ]

class LanguageParser ( Parser ):

    grammarFileName = "Language.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "','", "'read'", "'write'", "'{'", 
                     "'}'", "'if'", "'('", "')'", "'else'", "'while'", "'!'", 
                     "'<'", "'>'", "'=='", "'!='", "'&&'", "'||'", "'='", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'*'", "'/'", "'+'", "'-'", "'%'", "'.'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "INT_LITERAL", "FLOAT_LITERAL", "BOOL_LITERAL", "WS", 
                      "SINGLE_LINE_COMMENT", "STRING_LITERAL", "TYPE", "IDENTIFIER", 
                      "MUL", "DIV", "ADD", "SUB", "MOD", "CONCAT" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_declaration = 2
    RULE_read_statement = 3
    RULE_write_statement = 4
    RULE_block = 5
    RULE_conditional = 6
    RULE_while_loop = 7
    RULE_expression = 8
    RULE_assignment = 9
    RULE_literal = 10

    ruleNames =  [ "program", "statement", "declaration", "read_statement", 
                   "write_statement", "block", "conditional", "while_loop", 
                   "expression", "assignment", "literal" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    INT_LITERAL=20
    FLOAT_LITERAL=21
    BOOL_LITERAL=22
    WS=23
    SINGLE_LINE_COMMENT=24
    STRING_LITERAL=25
    TYPE=26
    IDENTIFIER=27
    MUL=28
    DIV=29
    ADD=30
    SUB=31
    MOD=32
    CONCAT=33

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(LanguageParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LanguageParser.StatementContext)
            else:
                return self.getTypedRuleContext(LanguageParser.StatementContext,i)


        def getRuleIndex(self):
            return LanguageParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = LanguageParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 22
                self.statement()
                self.state = 25 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 2406488506) != 0)):
                    break

            self.state = 27
            self.match(LanguageParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self):
            return self.getTypedRuleContext(LanguageParser.DeclarationContext,0)


        def expression(self):
            return self.getTypedRuleContext(LanguageParser.ExpressionContext,0)


        def read_statement(self):
            return self.getTypedRuleContext(LanguageParser.Read_statementContext,0)


        def write_statement(self):
            return self.getTypedRuleContext(LanguageParser.Write_statementContext,0)


        def block(self):
            return self.getTypedRuleContext(LanguageParser.BlockContext,0)


        def conditional(self):
            return self.getTypedRuleContext(LanguageParser.ConditionalContext,0)


        def while_loop(self):
            return self.getTypedRuleContext(LanguageParser.While_loopContext,0)


        def SINGLE_LINE_COMMENT(self):
            return self.getToken(LanguageParser.SINGLE_LINE_COMMENT, 0)

        def getRuleIndex(self):
            return LanguageParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = LanguageParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 40
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 29
                self.match(LanguageParser.T__0)
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 2)
                self.state = 30
                self.declaration()
                pass
            elif token in [8, 12, 20, 21, 22, 25, 27, 31]:
                self.enterOuterAlt(localctx, 3)
                self.state = 31
                self.expression(0)
                self.state = 32
                self.match(LanguageParser.T__0)
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 4)
                self.state = 34
                self.read_statement()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 5)
                self.state = 35
                self.write_statement()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 6)
                self.state = 36
                self.block()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 7)
                self.state = 37
                self.conditional()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 8)
                self.state = 38
                self.while_loop()
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 9)
                self.state = 39
                self.match(LanguageParser.SINGLE_LINE_COMMENT)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(LanguageParser.TYPE, 0)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(LanguageParser.IDENTIFIER)
            else:
                return self.getToken(LanguageParser.IDENTIFIER, i)

        def getRuleIndex(self):
            return LanguageParser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = LanguageParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(LanguageParser.TYPE)
            self.state = 43
            self.match(LanguageParser.IDENTIFIER)
            self.state = 48
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 44
                self.match(LanguageParser.T__1)
                self.state = 45
                self.match(LanguageParser.IDENTIFIER)
                self.state = 50
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 51
            self.match(LanguageParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Read_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(LanguageParser.IDENTIFIER)
            else:
                return self.getToken(LanguageParser.IDENTIFIER, i)

        def getRuleIndex(self):
            return LanguageParser.RULE_read_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRead_statement" ):
                listener.enterRead_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRead_statement" ):
                listener.exitRead_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRead_statement" ):
                return visitor.visitRead_statement(self)
            else:
                return visitor.visitChildren(self)




    def read_statement(self):

        localctx = LanguageParser.Read_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_read_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(LanguageParser.T__2)
            self.state = 54
            self.match(LanguageParser.IDENTIFIER)
            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 55
                self.match(LanguageParser.T__1)
                self.state = 56
                self.match(LanguageParser.IDENTIFIER)
                self.state = 61
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 62
            self.match(LanguageParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Write_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LanguageParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LanguageParser.ExpressionContext,i)


        def getRuleIndex(self):
            return LanguageParser.RULE_write_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWrite_statement" ):
                listener.enterWrite_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWrite_statement" ):
                listener.exitWrite_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWrite_statement" ):
                return visitor.visitWrite_statement(self)
            else:
                return visitor.visitChildren(self)




    def write_statement(self):

        localctx = LanguageParser.Write_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_write_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(LanguageParser.T__3)
            self.state = 65
            self.expression(0)
            self.state = 70
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 66
                self.match(LanguageParser.T__1)
                self.state = 67
                self.expression(0)
                self.state = 72
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 73
            self.match(LanguageParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LanguageParser.StatementContext)
            else:
                return self.getTypedRuleContext(LanguageParser.StatementContext,i)


        def getRuleIndex(self):
            return LanguageParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = LanguageParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(LanguageParser.T__4)
            self.state = 79
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2406488506) != 0):
                self.state = 76
                self.statement()
                self.state = 81
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 82
            self.match(LanguageParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(LanguageParser.ExpressionContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LanguageParser.StatementContext)
            else:
                return self.getTypedRuleContext(LanguageParser.StatementContext,i)


        def getRuleIndex(self):
            return LanguageParser.RULE_conditional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditional" ):
                listener.enterConditional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditional" ):
                listener.exitConditional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditional" ):
                return visitor.visitConditional(self)
            else:
                return visitor.visitChildren(self)




    def conditional(self):

        localctx = LanguageParser.ConditionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_conditional)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(LanguageParser.T__6)
            self.state = 85
            self.match(LanguageParser.T__7)
            self.state = 86
            self.expression(0)
            self.state = 87
            self.match(LanguageParser.T__8)
            self.state = 88
            self.statement()
            self.state = 91
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 89
                self.match(LanguageParser.T__9)
                self.state = 90
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_loopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(LanguageParser.ExpressionContext,0)


        def statement(self):
            return self.getTypedRuleContext(LanguageParser.StatementContext,0)


        def getRuleIndex(self):
            return LanguageParser.RULE_while_loop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_loop" ):
                listener.enterWhile_loop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_loop" ):
                listener.exitWhile_loop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_loop" ):
                return visitor.visitWhile_loop(self)
            else:
                return visitor.visitChildren(self)




    def while_loop(self):

        localctx = LanguageParser.While_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_while_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(LanguageParser.T__10)
            self.state = 94
            self.match(LanguageParser.T__7)
            self.state = 95
            self.expression(0)
            self.state = 96
            self.match(LanguageParser.T__8)
            self.state = 97
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.prefix = None # Token
            self.op = None # Token

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LanguageParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LanguageParser.ExpressionContext,i)


        def SUB(self):
            return self.getToken(LanguageParser.SUB, 0)

        def assignment(self):
            return self.getTypedRuleContext(LanguageParser.AssignmentContext,0)


        def IDENTIFIER(self):
            return self.getToken(LanguageParser.IDENTIFIER, 0)

        def literal(self):
            return self.getTypedRuleContext(LanguageParser.LiteralContext,0)


        def MUL(self):
            return self.getToken(LanguageParser.MUL, 0)

        def DIV(self):
            return self.getToken(LanguageParser.DIV, 0)

        def MOD(self):
            return self.getToken(LanguageParser.MOD, 0)

        def ADD(self):
            return self.getToken(LanguageParser.ADD, 0)

        def CONCAT(self):
            return self.getToken(LanguageParser.CONCAT, 0)

        def getRuleIndex(self):
            return LanguageParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LanguageParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 100
                localctx.prefix = self.match(LanguageParser.SUB)
                self.state = 101
                self.expression(12)
                pass

            elif la_ == 2:
                self.state = 102
                localctx.prefix = self.match(LanguageParser.T__11)
                self.state = 103
                self.expression(11)
                pass

            elif la_ == 3:
                self.state = 104
                self.match(LanguageParser.T__7)
                self.state = 105
                self.expression(0)
                self.state = 106
                self.match(LanguageParser.T__8)
                pass

            elif la_ == 4:
                self.state = 108
                self.assignment()
                pass

            elif la_ == 5:
                self.state = 109
                self.match(LanguageParser.IDENTIFIER)
                pass

            elif la_ == 6:
                self.state = 110
                self.literal()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 133
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 131
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = LanguageParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 113
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 114
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 5100273664) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 115
                        self.expression(11)
                        pass

                    elif la_ == 2:
                        localctx = LanguageParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 116
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 117
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 11811160064) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 118
                        self.expression(10)
                        pass

                    elif la_ == 3:
                        localctx = LanguageParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 119
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 120
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==13 or _la==14):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 121
                        self.expression(9)
                        pass

                    elif la_ == 4:
                        localctx = LanguageParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 122
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 123
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==15 or _la==16):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 124
                        self.expression(8)
                        pass

                    elif la_ == 5:
                        localctx = LanguageParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 125
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 126
                        localctx.op = self.match(LanguageParser.T__16)
                        self.state = 127
                        self.expression(7)
                        pass

                    elif la_ == 6:
                        localctx = LanguageParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 128
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 129
                        localctx.op = self.match(LanguageParser.T__17)
                        self.state = 130
                        self.expression(6)
                        pass

             
                self.state = 135
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(LanguageParser.IDENTIFIER, 0)

        def expression(self):
            return self.getTypedRuleContext(LanguageParser.ExpressionContext,0)


        def getRuleIndex(self):
            return LanguageParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = LanguageParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.match(LanguageParser.IDENTIFIER)
            self.state = 137
            self.match(LanguageParser.T__18)
            self.state = 138
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOAT_LITERAL(self):
            return self.getToken(LanguageParser.FLOAT_LITERAL, 0)

        def INT_LITERAL(self):
            return self.getToken(LanguageParser.INT_LITERAL, 0)

        def BOOL_LITERAL(self):
            return self.getToken(LanguageParser.BOOL_LITERAL, 0)

        def STRING_LITERAL(self):
            return self.getToken(LanguageParser.STRING_LITERAL, 0)

        def getRuleIndex(self):
            return LanguageParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = LanguageParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 40894464) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[8] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 5)
         




