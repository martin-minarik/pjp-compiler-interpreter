import sys
from antlr4 import *
from LanguageLexer import LanguageLexer
from LanguageParser import LanguageParser
from pprint import pprint
from antlr4.tree.Trees import Trees

class VerboseErrorListener(DiagnosticErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        stack = recognizer.getRuleInvocationStack()
        stack.reverse()
        print("Rule stack: {}".format(stack))
        print("line {}:{} at {}: {}".format(line, column, offendingSymbol, msg))
        print()

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = LanguageLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = LanguageParser(stream)
    # parser.removeErrorListeners()  # Remove default error listeners
    # parser.addErrorListener(VerboseErrorListener())  # Add custom listener
    tree = parser.program()
    if parser.getNumberOfSyntaxErrors() > 0:
        print("syntax errors")
    else:
        print("Grammar is Ok")
        print(Trees.toStringTree(tree, None, parser))


if __name__ == '__main__':
    main(sys.argv)
