import sys
from pprint import pprint

from antlr4 import *
from antlr4.tree.Trees import Trees

from errors import Errors
from language.LanguageLexer import LanguageLexer
from language.LanguageParser import LanguageParser
from stop_parsing_error_listener import StopParsingListener
from typecheck_visitor import TypeCheckingVisitor
from output_visitor import OutputVisitor
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

        typecheck_visitor = TypeCheckingVisitor()
        typecheck_visitor.visit(tree)

        # pprint(visitor.symbol_table.memory)

        if Errors.number_of_errors():
            Errors.print_and_clear_errors()
            return

        print("Type Checking is Ok")


        print("OutputVisitor:")
        output_visitor = OutputVisitor()
        # output = output_visitor.visit(tree)
        # print(output)


if __name__ == "__main__":
    main(sys.argv)
