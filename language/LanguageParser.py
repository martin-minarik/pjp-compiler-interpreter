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
        4,1,36,142,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,4,0,22,8,0,11,0,12,0,23,1,0,1,0,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,39,8,1,1,2,1,2,1,2,
        1,2,5,2,45,8,2,10,2,12,2,48,9,2,1,2,1,2,1,3,1,3,1,3,1,3,5,3,56,8,
        3,10,3,12,3,59,9,3,1,3,1,3,1,4,1,4,1,4,1,4,5,4,67,8,4,10,4,12,4,
        70,9,4,1,4,1,4,1,5,1,5,5,5,76,8,5,10,5,12,5,79,9,5,1,5,1,5,1,6,1,
        6,1,6,1,6,1,6,1,6,1,6,3,6,90,8,6,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,
        1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,
        115,8,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,
        1,8,1,8,1,8,1,8,5,8,135,8,8,10,8,12,8,138,9,8,1,9,1,9,1,9,0,1,16,
        10,0,2,4,6,8,10,12,14,16,18,0,5,2,0,25,26,29,29,2,0,27,28,30,30,
        1,0,35,36,1,0,31,32,1,0,14,17,159,0,21,1,0,0,0,2,38,1,0,0,0,4,40,
        1,0,0,0,6,51,1,0,0,0,8,62,1,0,0,0,10,73,1,0,0,0,12,82,1,0,0,0,14,
        91,1,0,0,0,16,114,1,0,0,0,18,139,1,0,0,0,20,22,3,2,1,0,21,20,1,0,
        0,0,22,23,1,0,0,0,23,21,1,0,0,0,23,24,1,0,0,0,24,25,1,0,0,0,25,26,
        5,0,0,1,26,1,1,0,0,0,27,39,5,1,0,0,28,39,3,4,2,0,29,30,3,16,8,0,
        30,31,5,1,0,0,31,39,1,0,0,0,32,39,3,6,3,0,33,39,3,8,4,0,34,39,3,
        10,5,0,35,39,3,12,6,0,36,39,3,14,7,0,37,39,5,21,0,0,38,27,1,0,0,
        0,38,28,1,0,0,0,38,29,1,0,0,0,38,32,1,0,0,0,38,33,1,0,0,0,38,34,
        1,0,0,0,38,35,1,0,0,0,38,36,1,0,0,0,38,37,1,0,0,0,39,3,1,0,0,0,40,
        41,3,18,9,0,41,46,5,23,0,0,42,43,5,2,0,0,43,45,5,23,0,0,44,42,1,
        0,0,0,45,48,1,0,0,0,46,44,1,0,0,0,46,47,1,0,0,0,47,49,1,0,0,0,48,
        46,1,0,0,0,49,50,5,1,0,0,50,5,1,0,0,0,51,52,5,3,0,0,52,57,5,23,0,
        0,53,54,5,2,0,0,54,56,5,23,0,0,55,53,1,0,0,0,56,59,1,0,0,0,57,55,
        1,0,0,0,57,58,1,0,0,0,58,60,1,0,0,0,59,57,1,0,0,0,60,61,5,1,0,0,
        61,7,1,0,0,0,62,63,5,4,0,0,63,68,3,16,8,0,64,65,5,2,0,0,65,67,3,
        16,8,0,66,64,1,0,0,0,67,70,1,0,0,0,68,66,1,0,0,0,68,69,1,0,0,0,69,
        71,1,0,0,0,70,68,1,0,0,0,71,72,5,1,0,0,72,9,1,0,0,0,73,77,5,5,0,
        0,74,76,3,2,1,0,75,74,1,0,0,0,76,79,1,0,0,0,77,75,1,0,0,0,77,78,
        1,0,0,0,78,80,1,0,0,0,79,77,1,0,0,0,80,81,5,6,0,0,81,11,1,0,0,0,
        82,83,5,7,0,0,83,84,5,8,0,0,84,85,3,16,8,0,85,86,5,9,0,0,86,89,3,
        2,1,0,87,88,5,10,0,0,88,90,3,2,1,0,89,87,1,0,0,0,89,90,1,0,0,0,90,
        13,1,0,0,0,91,92,5,11,0,0,92,93,5,8,0,0,93,94,3,16,8,0,94,95,5,9,
        0,0,95,96,3,2,1,0,96,15,1,0,0,0,97,98,6,8,-1,0,98,99,5,28,0,0,99,
        115,3,16,8,15,100,101,5,12,0,0,101,115,3,16,8,14,102,115,5,18,0,
        0,103,115,5,19,0,0,104,115,5,20,0,0,105,115,5,22,0,0,106,115,5,23,
        0,0,107,108,5,8,0,0,108,109,3,16,8,0,109,110,5,9,0,0,110,115,1,0,
        0,0,111,112,5,23,0,0,112,113,5,13,0,0,113,115,3,16,8,1,114,97,1,
        0,0,0,114,100,1,0,0,0,114,102,1,0,0,0,114,103,1,0,0,0,114,104,1,
        0,0,0,114,105,1,0,0,0,114,106,1,0,0,0,114,107,1,0,0,0,114,111,1,
        0,0,0,115,136,1,0,0,0,116,117,10,13,0,0,117,118,7,0,0,0,118,135,
        3,16,8,14,119,120,10,12,0,0,120,121,7,1,0,0,121,135,3,16,8,13,122,
        123,10,11,0,0,123,124,7,2,0,0,124,135,3,16,8,12,125,126,10,10,0,
        0,126,127,7,3,0,0,127,135,3,16,8,11,128,129,10,9,0,0,129,130,5,33,
        0,0,130,135,3,16,8,10,131,132,10,8,0,0,132,133,5,34,0,0,133,135,
        3,16,8,9,134,116,1,0,0,0,134,119,1,0,0,0,134,122,1,0,0,0,134,125,
        1,0,0,0,134,128,1,0,0,0,134,131,1,0,0,0,135,138,1,0,0,0,136,134,
        1,0,0,0,136,137,1,0,0,0,137,17,1,0,0,0,138,136,1,0,0,0,139,140,7,
        4,0,0,140,19,1,0,0,0,10,23,38,46,57,68,77,89,114,134,136
    ]

class LanguageParser ( Parser ):

    grammarFileName = "Language.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "','", "'read'", "'write'", "'{'", 
                     "'}'", "'if'", "'('", "')'", "'else'", "'while'", "'!'", 
                     "'='", "'int'", "'float'", "'bool'", "'string'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'*'", "'/'", "'+'", "'-'", 
                     "'%'", "'.'", "'=='", "'!='", "'&&'", "'||'", "'>'", 
                     "'<'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "INT_LITERAL", "FLOAT_LITERAL", 
                      "BOOL_LITERAL", "SINGLE_LINE_COMMENT", "STRING_LITERAL", 
                      "IDENTIFIER", "WS", "MUL", "DIV", "ADD", "SUB", "MOD", 
                      "CONCAT", "EQUAL", "NOTEQUAL", "AND", "OR", "GT", 
                      "LT" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_declaration = 2
    RULE_read_statement = 3
    RULE_write_statement = 4
    RULE_block = 5
    RULE_conditional = 6
    RULE_while_loop = 7
    RULE_expression = 8
    RULE_type_keyword = 9

    ruleNames =  [ "program", "statement", "declaration", "read_statement", 
                   "write_statement", "block", "conditional", "while_loop", 
                   "expression", "type_keyword" ]

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
    INT_LITERAL=18
    FLOAT_LITERAL=19
    BOOL_LITERAL=20
    SINGLE_LINE_COMMENT=21
    STRING_LITERAL=22
    IDENTIFIER=23
    WS=24
    MUL=25
    DIV=26
    ADD=27
    SUB=28
    MOD=29
    CONCAT=30
    EQUAL=31
    NOTEQUAL=32
    AND=33
    OR=34
    GT=35
    LT=36

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
            self.state = 21 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 20
                self.statement()
                self.state = 23 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 285202874) != 0)):
                    break

            self.state = 25
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
            self.state = 38
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 27
                self.match(LanguageParser.T__0)
                pass
            elif token in [14, 15, 16, 17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 28
                self.declaration()
                pass
            elif token in [8, 12, 18, 19, 20, 22, 23, 28]:
                self.enterOuterAlt(localctx, 3)
                self.state = 29
                self.expression(0)
                self.state = 30
                self.match(LanguageParser.T__0)
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 4)
                self.state = 32
                self.read_statement()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 5)
                self.state = 33
                self.write_statement()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 6)
                self.state = 34
                self.block()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 7)
                self.state = 35
                self.conditional()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 8)
                self.state = 36
                self.while_loop()
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 9)
                self.state = 37
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

        def type_keyword(self):
            return self.getTypedRuleContext(LanguageParser.Type_keywordContext,0)


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
            self.state = 40
            self.type_keyword()
            self.state = 41
            self.match(LanguageParser.IDENTIFIER)
            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 42
                self.match(LanguageParser.T__1)
                self.state = 43
                self.match(LanguageParser.IDENTIFIER)
                self.state = 48
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 49
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
            self.state = 51
            self.match(LanguageParser.T__2)
            self.state = 52
            self.match(LanguageParser.IDENTIFIER)
            self.state = 57
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 53
                self.match(LanguageParser.T__1)
                self.state = 54
                self.match(LanguageParser.IDENTIFIER)
                self.state = 59
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 60
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
            self.state = 62
            self.match(LanguageParser.T__3)
            self.state = 63
            self.expression(0)
            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 64
                self.match(LanguageParser.T__1)
                self.state = 65
                self.expression(0)
                self.state = 70
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 71
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
            self.state = 73
            self.match(LanguageParser.T__4)
            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 285202874) != 0):
                self.state = 74
                self.statement()
                self.state = 79
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 80
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
            self.state = 82
            self.match(LanguageParser.T__6)
            self.state = 83
            self.match(LanguageParser.T__7)
            self.state = 84
            self.expression(0)
            self.state = 85
            self.match(LanguageParser.T__8)
            self.state = 86
            self.statement()
            self.state = 89
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 87
                self.match(LanguageParser.T__9)
                self.state = 88
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
            self.state = 91
            self.match(LanguageParser.T__10)
            self.state = 92
            self.match(LanguageParser.T__7)
            self.state = 93
            self.expression(0)
            self.state = 94
            self.match(LanguageParser.T__8)
            self.state = 95
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


        def getRuleIndex(self):
            return LanguageParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class MulDivModContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LanguageParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LanguageParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LanguageParser.ExpressionContext,i)

        def MUL(self):
            return self.getToken(LanguageParser.MUL, 0)
        def DIV(self):
            return self.getToken(LanguageParser.DIV, 0)
        def MOD(self):
            return self.getToken(LanguageParser.MOD, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDivMod" ):
                listener.enterMulDivMod(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDivMod" ):
                listener.exitMulDivMod(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDivMod" ):
                return visitor.visitMulDivMod(self)
            else:
                return visitor.visitChildren(self)


    class ParenthesesContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LanguageParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(LanguageParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParentheses" ):
                listener.enterParentheses(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParentheses" ):
                listener.exitParentheses(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParentheses" ):
                return visitor.visitParentheses(self)
            else:
                return visitor.visitChildren(self)


    class LogicalNotContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LanguageParser.ExpressionContext
            super().__init__(parser)
            self.prefix = None # Token
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(LanguageParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalNot" ):
                listener.enterLogicalNot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalNot" ):
                listener.exitLogicalNot(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalNot" ):
                return visitor.visitLogicalNot(self)
            else:
                return visitor.visitChildren(self)


    class EqualNotEqualContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LanguageParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LanguageParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LanguageParser.ExpressionContext,i)

        def EQUAL(self):
            return self.getToken(LanguageParser.EQUAL, 0)
        def NOTEQUAL(self):
            return self.getToken(LanguageParser.NOTEQUAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqualNotEqual" ):
                listener.enterEqualNotEqual(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqualNotEqual" ):
                listener.exitEqualNotEqual(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqualNotEqual" ):
                return visitor.visitEqualNotEqual(self)
            else:
                return visitor.visitChildren(self)


    class AddSubConcatContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LanguageParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LanguageParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LanguageParser.ExpressionContext,i)

        def ADD(self):
            return self.getToken(LanguageParser.ADD, 0)
        def SUB(self):
            return self.getToken(LanguageParser.SUB, 0)
        def CONCAT(self):
            return self.getToken(LanguageParser.CONCAT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSubConcat" ):
                listener.enterAddSubConcat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSubConcat" ):
                listener.exitAddSubConcat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSubConcat" ):
                return visitor.visitAddSubConcat(self)
            else:
                return visitor.visitChildren(self)


    class AssignmentContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LanguageParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(LanguageParser.IDENTIFIER, 0)
        def expression(self):
            return self.getTypedRuleContext(LanguageParser.ExpressionContext,0)


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


    class IntLiteralContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LanguageParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT_LITERAL(self):
            return self.getToken(LanguageParser.INT_LITERAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntLiteral" ):
                listener.enterIntLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntLiteral" ):
                listener.exitIntLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntLiteral" ):
                return visitor.visitIntLiteral(self)
            else:
                return visitor.visitChildren(self)


    class LesserGreaterContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LanguageParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LanguageParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LanguageParser.ExpressionContext,i)

        def LT(self):
            return self.getToken(LanguageParser.LT, 0)
        def GT(self):
            return self.getToken(LanguageParser.GT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLesserGreater" ):
                listener.enterLesserGreater(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLesserGreater" ):
                listener.exitLesserGreater(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLesserGreater" ):
                return visitor.visitLesserGreater(self)
            else:
                return visitor.visitChildren(self)


    class LogicalAndContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LanguageParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LanguageParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LanguageParser.ExpressionContext,i)

        def AND(self):
            return self.getToken(LanguageParser.AND, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalAnd" ):
                listener.enterLogicalAnd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalAnd" ):
                listener.exitLogicalAnd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalAnd" ):
                return visitor.visitLogicalAnd(self)
            else:
                return visitor.visitChildren(self)


    class BoolLiteralContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LanguageParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOOL_LITERAL(self):
            return self.getToken(LanguageParser.BOOL_LITERAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolLiteral" ):
                listener.enterBoolLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolLiteral" ):
                listener.exitBoolLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolLiteral" ):
                return visitor.visitBoolLiteral(self)
            else:
                return visitor.visitChildren(self)


    class StringLiteralContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LanguageParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING_LITERAL(self):
            return self.getToken(LanguageParser.STRING_LITERAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringLiteral" ):
                listener.enterStringLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringLiteral" ):
                listener.exitStringLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringLiteral" ):
                return visitor.visitStringLiteral(self)
            else:
                return visitor.visitChildren(self)


    class UnaryMinusContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LanguageParser.ExpressionContext
            super().__init__(parser)
            self.prefix = None # Token
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(LanguageParser.ExpressionContext,0)

        def SUB(self):
            return self.getToken(LanguageParser.SUB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryMinus" ):
                listener.enterUnaryMinus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryMinus" ):
                listener.exitUnaryMinus(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryMinus" ):
                return visitor.visitUnaryMinus(self)
            else:
                return visitor.visitChildren(self)


    class FloatLiteralContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LanguageParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT_LITERAL(self):
            return self.getToken(LanguageParser.FLOAT_LITERAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloatLiteral" ):
                listener.enterFloatLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloatLiteral" ):
                listener.exitFloatLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloatLiteral" ):
                return visitor.visitFloatLiteral(self)
            else:
                return visitor.visitChildren(self)


    class IdContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LanguageParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(LanguageParser.IDENTIFIER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId" ):
                listener.enterId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId" ):
                listener.exitId(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId" ):
                return visitor.visitId(self)
            else:
                return visitor.visitChildren(self)


    class LogicalOrContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LanguageParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LanguageParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LanguageParser.ExpressionContext,i)

        def OR(self):
            return self.getToken(LanguageParser.OR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalOr" ):
                listener.enterLogicalOr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalOr" ):
                listener.exitLogicalOr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalOr" ):
                return visitor.visitLogicalOr(self)
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
            self.state = 114
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                localctx = LanguageParser.UnaryMinusContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 98
                localctx.prefix = self.match(LanguageParser.SUB)
                self.state = 99
                self.expression(15)
                pass

            elif la_ == 2:
                localctx = LanguageParser.LogicalNotContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 100
                localctx.prefix = self.match(LanguageParser.T__11)
                self.state = 101
                self.expression(14)
                pass

            elif la_ == 3:
                localctx = LanguageParser.IntLiteralContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 102
                self.match(LanguageParser.INT_LITERAL)
                pass

            elif la_ == 4:
                localctx = LanguageParser.FloatLiteralContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 103
                self.match(LanguageParser.FLOAT_LITERAL)
                pass

            elif la_ == 5:
                localctx = LanguageParser.BoolLiteralContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 104
                self.match(LanguageParser.BOOL_LITERAL)
                pass

            elif la_ == 6:
                localctx = LanguageParser.StringLiteralContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 105
                self.match(LanguageParser.STRING_LITERAL)
                pass

            elif la_ == 7:
                localctx = LanguageParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 106
                self.match(LanguageParser.IDENTIFIER)
                pass

            elif la_ == 8:
                localctx = LanguageParser.ParenthesesContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 107
                self.match(LanguageParser.T__7)
                self.state = 108
                self.expression(0)
                self.state = 109
                self.match(LanguageParser.T__8)
                pass

            elif la_ == 9:
                localctx = LanguageParser.AssignmentContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 111
                self.match(LanguageParser.IDENTIFIER)
                self.state = 112
                self.match(LanguageParser.T__12)
                self.state = 113
                self.expression(1)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 136
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 134
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = LanguageParser.MulDivModContext(self, LanguageParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 116
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 117
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 637534208) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 118
                        self.expression(14)
                        pass

                    elif la_ == 2:
                        localctx = LanguageParser.AddSubConcatContext(self, LanguageParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 119
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 120
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1476395008) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 121
                        self.expression(13)
                        pass

                    elif la_ == 3:
                        localctx = LanguageParser.LesserGreaterContext(self, LanguageParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 122
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 123
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==35 or _la==36):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 124
                        self.expression(12)
                        pass

                    elif la_ == 4:
                        localctx = LanguageParser.EqualNotEqualContext(self, LanguageParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 125
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 126
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==31 or _la==32):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 127
                        self.expression(11)
                        pass

                    elif la_ == 5:
                        localctx = LanguageParser.LogicalAndContext(self, LanguageParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 128
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 129
                        localctx.op = self.match(LanguageParser.AND)
                        self.state = 130
                        self.expression(10)
                        pass

                    elif la_ == 6:
                        localctx = LanguageParser.LogicalOrContext(self, LanguageParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 131
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 132
                        localctx.op = self.match(LanguageParser.OR)
                        self.state = 133
                        self.expression(9)
                        pass

             
                self.state = 138
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Type_keywordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LanguageParser.RULE_type_keyword

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_keyword" ):
                listener.enterType_keyword(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_keyword" ):
                listener.exitType_keyword(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_keyword" ):
                return visitor.visitType_keyword(self)
            else:
                return visitor.visitChildren(self)




    def type_keyword(self):

        localctx = LanguageParser.Type_keywordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_type_keyword)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 245760) != 0)):
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
                return self.precpred(self._ctx, 13)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 8)
         




