import sys
from pprint import pprint

from antlr4 import *
from antlr4.tree.Trees import Trees

from LanguageLexer import LanguageLexer
from LanguageParser import LanguageParser
from stop_parsing_error_listener import StopParsingListener
from verbose_error_listener import VerboseErrorListener


def main(argv):
    input_stream = FileStream(argv[1])
    lexer = LanguageLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = LanguageParser(stream)

    # Error listeners
    # parser.removeErrorListeners()  # Remove default error listeners
    # parser.addErrorListener(VerboseErrorListener())
    # parser.addErrorListener(StopParsingListener())

    tree = parser.program()

    if parser.getNumberOfSyntaxErrors() > 0:
        print("syntax errors")
    else:
        print("Grammar is Ok")
        print(Trees.toStringTree(tree, None, parser))


if __name__ == '__main__':
    main(sys.argv)
