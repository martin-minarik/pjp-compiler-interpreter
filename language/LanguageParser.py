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
        4,1,36,151,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,4,0,26,8,0,11,
        0,12,0,27,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,
        1,43,8,1,1,2,1,2,1,2,1,2,5,2,49,8,2,10,2,12,2,52,9,2,1,2,1,2,1,3,
        1,3,1,3,1,3,5,3,60,8,3,10,3,12,3,63,9,3,1,3,1,3,1,4,1,4,1,4,1,4,
        5,4,71,8,4,10,4,12,4,74,9,4,1,4,1,4,1,5,1,5,5,5,80,8,5,10,5,12,5,
        83,9,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,94,8,6,1,7,1,7,1,
        7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,
        8,114,8,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,
        8,1,8,1,8,1,8,1,8,5,8,134,8,8,10,8,12,8,137,9,8,1,9,1,9,1,9,1,9,
        1,10,1,10,1,11,1,11,1,11,1,11,3,11,149,8,11,1,11,0,1,16,12,0,2,4,
        6,8,10,12,14,16,18,20,22,0,5,2,0,31,32,35,35,2,0,33,34,36,36,1,0,
        13,14,1,0,15,16,1,0,20,23,166,0,25,1,0,0,0,2,42,1,0,0,0,4,44,1,0,
        0,0,6,55,1,0,0,0,8,66,1,0,0,0,10,77,1,0,0,0,12,86,1,0,0,0,14,95,
        1,0,0,0,16,113,1,0,0,0,18,138,1,0,0,0,20,142,1,0,0,0,22,148,1,0,
        0,0,24,26,3,2,1,0,25,24,1,0,0,0,26,27,1,0,0,0,27,25,1,0,0,0,27,28,
        1,0,0,0,28,29,1,0,0,0,29,30,5,0,0,1,30,1,1,0,0,0,31,43,5,1,0,0,32,
        43,3,4,2,0,33,34,3,16,8,0,34,35,5,1,0,0,35,43,1,0,0,0,36,43,3,6,
        3,0,37,43,3,8,4,0,38,43,3,10,5,0,39,43,3,12,6,0,40,43,3,14,7,0,41,
        43,5,27,0,0,42,31,1,0,0,0,42,32,1,0,0,0,42,33,1,0,0,0,42,36,1,0,
        0,0,42,37,1,0,0,0,42,38,1,0,0,0,42,39,1,0,0,0,42,40,1,0,0,0,42,41,
        1,0,0,0,43,3,1,0,0,0,44,45,3,20,10,0,45,50,5,29,0,0,46,47,5,2,0,
        0,47,49,5,29,0,0,48,46,1,0,0,0,49,52,1,0,0,0,50,48,1,0,0,0,50,51,
        1,0,0,0,51,53,1,0,0,0,52,50,1,0,0,0,53,54,5,1,0,0,54,5,1,0,0,0,55,
        56,5,3,0,0,56,61,5,29,0,0,57,58,5,2,0,0,58,60,5,29,0,0,59,57,1,0,
        0,0,60,63,1,0,0,0,61,59,1,0,0,0,61,62,1,0,0,0,62,64,1,0,0,0,63,61,
        1,0,0,0,64,65,5,1,0,0,65,7,1,0,0,0,66,67,5,4,0,0,67,72,3,16,8,0,
        68,69,5,2,0,0,69,71,3,16,8,0,70,68,1,0,0,0,71,74,1,0,0,0,72,70,1,
        0,0,0,72,73,1,0,0,0,73,75,1,0,0,0,74,72,1,0,0,0,75,76,5,1,0,0,76,
        9,1,0,0,0,77,81,5,5,0,0,78,80,3,2,1,0,79,78,1,0,0,0,80,83,1,0,0,
        0,81,79,1,0,0,0,81,82,1,0,0,0,82,84,1,0,0,0,83,81,1,0,0,0,84,85,
        5,6,0,0,85,11,1,0,0,0,86,87,5,7,0,0,87,88,5,8,0,0,88,89,3,16,8,0,
        89,90,5,9,0,0,90,93,3,2,1,0,91,92,5,10,0,0,92,94,3,2,1,0,93,91,1,
        0,0,0,93,94,1,0,0,0,94,13,1,0,0,0,95,96,5,11,0,0,96,97,5,8,0,0,97,
        98,3,16,8,0,98,99,5,9,0,0,99,100,3,2,1,0,100,15,1,0,0,0,101,102,
        6,8,-1,0,102,103,5,34,0,0,103,114,3,16,8,12,104,105,5,12,0,0,105,
        114,3,16,8,11,106,107,5,8,0,0,107,108,3,16,8,0,108,109,5,9,0,0,109,
        114,1,0,0,0,110,114,3,18,9,0,111,114,5,29,0,0,112,114,3,22,11,0,
        113,101,1,0,0,0,113,104,1,0,0,0,113,106,1,0,0,0,113,110,1,0,0,0,
        113,111,1,0,0,0,113,112,1,0,0,0,114,135,1,0,0,0,115,116,10,10,0,
        0,116,117,7,0,0,0,117,134,3,16,8,11,118,119,10,9,0,0,119,120,7,1,
        0,0,120,134,3,16,8,10,121,122,10,8,0,0,122,123,7,2,0,0,123,134,3,
        16,8,9,124,125,10,7,0,0,125,126,7,3,0,0,126,134,3,16,8,8,127,128,
        10,6,0,0,128,129,5,17,0,0,129,134,3,16,8,7,130,131,10,5,0,0,131,
        132,5,18,0,0,132,134,3,16,8,6,133,115,1,0,0,0,133,118,1,0,0,0,133,
        121,1,0,0,0,133,124,1,0,0,0,133,127,1,0,0,0,133,130,1,0,0,0,134,
        137,1,0,0,0,135,133,1,0,0,0,135,136,1,0,0,0,136,17,1,0,0,0,137,135,
        1,0,0,0,138,139,5,29,0,0,139,140,5,19,0,0,140,141,3,16,8,0,141,19,
        1,0,0,0,142,143,7,4,0,0,143,21,1,0,0,0,144,149,5,24,0,0,145,149,
        5,25,0,0,146,149,5,26,0,0,147,149,5,28,0,0,148,144,1,0,0,0,148,145,
        1,0,0,0,148,146,1,0,0,0,148,147,1,0,0,0,149,23,1,0,0,0,11,27,42,
        50,61,72,81,93,113,133,135,148
    ]

class LanguageParser ( Parser ):

    grammarFileName = "Language.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "','", "'read'", "'write'", "'{'", 
                     "'}'", "'if'", "'('", "')'", "'else'", "'while'", "'!'", 
                     "'<'", "'>'", "'=='", "'!='", "'&&'", "'||'", "'='", 
                     "'int'", "'float'", "'bool'", "'string'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'*'", "'/'", "'+'", "'-'", 
                     "'%'", "'.'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "INT_LITERAL", "FLOAT_LITERAL", "BOOL_LITERAL", "SINGLE_LINE_COMMENT", 
                      "STRING_LITERAL", "IDENTIFIER", "WS", "MUL", "DIV", 
                      "ADD", "SUB", "MOD", "CONCAT" ]

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
    RULE_type_keyword = 10
    RULE_literal = 11

    ruleNames =  [ "program", "statement", "declaration", "read_statement", 
                   "write_statement", "block", "conditional", "while_loop", 
                   "expression", "assignment", "type_keyword", "literal" ]

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
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    INT_LITERAL=24
    FLOAT_LITERAL=25
    BOOL_LITERAL=26
    SINGLE_LINE_COMMENT=27
    STRING_LITERAL=28
    IDENTIFIER=29
    WS=30
    MUL=31
    DIV=32
    ADD=33
    SUB=34
    MOD=35
    CONCAT=36

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
            self.state = 25 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 24
                self.statement()
                self.state = 27 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 18252569018) != 0)):
                    break

            self.state = 29
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
            self.state = 42
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 31
                self.match(LanguageParser.T__0)
                pass
            elif token in [20, 21, 22, 23]:
                self.enterOuterAlt(localctx, 2)
                self.state = 32
                self.declaration()
                pass
            elif token in [8, 12, 24, 25, 26, 28, 29, 34]:
                self.enterOuterAlt(localctx, 3)
                self.state = 33
                self.expression(0)
                self.state = 34
                self.match(LanguageParser.T__0)
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 4)
                self.state = 36
                self.read_statement()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 5)
                self.state = 37
                self.write_statement()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 6)
                self.state = 38
                self.block()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 7)
                self.state = 39
                self.conditional()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 8)
                self.state = 40
                self.while_loop()
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 9)
                self.state = 41
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
            self.state = 44
            self.type_keyword()
            self.state = 45
            self.match(LanguageParser.IDENTIFIER)
            self.state = 50
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 46
                self.match(LanguageParser.T__1)
                self.state = 47
                self.match(LanguageParser.IDENTIFIER)
                self.state = 52
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 53
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
            self.state = 55
            self.match(LanguageParser.T__2)
            self.state = 56
            self.match(LanguageParser.IDENTIFIER)
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 57
                self.match(LanguageParser.T__1)
                self.state = 58
                self.match(LanguageParser.IDENTIFIER)
                self.state = 63
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 64
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
            self.state = 66
            self.match(LanguageParser.T__3)
            self.state = 67
            self.expression(0)
            self.state = 72
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 68
                self.match(LanguageParser.T__1)
                self.state = 69
                self.expression(0)
                self.state = 74
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 75
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
            self.state = 77
            self.match(LanguageParser.T__4)
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 18252569018) != 0):
                self.state = 78
                self.statement()
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 84
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
            self.state = 86
            self.match(LanguageParser.T__6)
            self.state = 87
            self.match(LanguageParser.T__7)
            self.state = 88
            self.expression(0)
            self.state = 89
            self.match(LanguageParser.T__8)
            self.state = 90
            self.statement()
            self.state = 93
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 91
                self.match(LanguageParser.T__9)
                self.state = 92
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
            self.state = 95
            self.match(LanguageParser.T__10)
            self.state = 96
            self.match(LanguageParser.T__7)
            self.state = 97
            self.expression(0)
            self.state = 98
            self.match(LanguageParser.T__8)
            self.state = 99
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
            self.state = 113
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 102
                localctx.prefix = self.match(LanguageParser.SUB)
                self.state = 103
                self.expression(12)
                pass

            elif la_ == 2:
                self.state = 104
                localctx.prefix = self.match(LanguageParser.T__11)
                self.state = 105
                self.expression(11)
                pass

            elif la_ == 3:
                self.state = 106
                self.match(LanguageParser.T__7)
                self.state = 107
                self.expression(0)
                self.state = 108
                self.match(LanguageParser.T__8)
                pass

            elif la_ == 4:
                self.state = 110
                self.assignment()
                pass

            elif la_ == 5:
                self.state = 111
                self.match(LanguageParser.IDENTIFIER)
                pass

            elif la_ == 6:
                self.state = 112
                self.literal()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 135
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 133
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = LanguageParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 115
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 116
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 40802189312) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 117
                        self.expression(11)
                        pass

                    elif la_ == 2:
                        localctx = LanguageParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 118
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 119
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 94489280512) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 120
                        self.expression(10)
                        pass

                    elif la_ == 3:
                        localctx = LanguageParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 121
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 122
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==13 or _la==14):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 123
                        self.expression(9)
                        pass

                    elif la_ == 4:
                        localctx = LanguageParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 124
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 125
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==15 or _la==16):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 126
                        self.expression(8)
                        pass

                    elif la_ == 5:
                        localctx = LanguageParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 127
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 128
                        localctx.op = self.match(LanguageParser.T__16)
                        self.state = 129
                        self.expression(7)
                        pass

                    elif la_ == 6:
                        localctx = LanguageParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 130
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 131
                        localctx.op = self.match(LanguageParser.T__17)
                        self.state = 132
                        self.expression(6)
                        pass

             
                self.state = 137
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
            self.state = 138
            self.match(LanguageParser.IDENTIFIER)
            self.state = 139
            self.match(LanguageParser.T__18)
            self.state = 140
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
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
        self.enterRule(localctx, 20, self.RULE_type_keyword)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 15728640) != 0)):
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


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LanguageParser.RULE_literal

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class BoolContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LanguageParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOOL_LITERAL(self):
            return self.getToken(LanguageParser.BOOL_LITERAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBool" ):
                listener.enterBool(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBool" ):
                listener.exitBool(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBool" ):
                return visitor.visitBool(self)
            else:
                return visitor.visitChildren(self)


    class StringContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LanguageParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING_LITERAL(self):
            return self.getToken(LanguageParser.STRING_LITERAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString" ):
                return visitor.visitString(self)
            else:
                return visitor.visitChildren(self)


    class FloatContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LanguageParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT_LITERAL(self):
            return self.getToken(LanguageParser.FLOAT_LITERAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloat" ):
                listener.enterFloat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloat" ):
                listener.exitFloat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloat" ):
                return visitor.visitFloat(self)
            else:
                return visitor.visitChildren(self)


    class IntContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LanguageParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT_LITERAL(self):
            return self.getToken(LanguageParser.INT_LITERAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt" ):
                return visitor.visitInt(self)
            else:
                return visitor.visitChildren(self)



    def literal(self):

        localctx = LanguageParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_literal)
        try:
            self.state = 148
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24]:
                localctx = LanguageParser.IntContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 144
                self.match(LanguageParser.INT_LITERAL)
                pass
            elif token in [25]:
                localctx = LanguageParser.FloatContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 145
                self.match(LanguageParser.FLOAT_LITERAL)
                pass
            elif token in [26]:
                localctx = LanguageParser.BoolContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 146
                self.match(LanguageParser.BOOL_LITERAL)
                pass
            elif token in [28]:
                localctx = LanguageParser.StringContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 147
                self.match(LanguageParser.STRING_LITERAL)
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
         




