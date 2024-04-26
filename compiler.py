import sys
from pprint import pprint

from antlr4 import *
from antlr4.tree.Trees import Trees

from errors import Errors
from language.LanguageLexer import LanguageLexer
from language.LanguageParser import LanguageParser
from output_visitor import OutputVisitor
from stop_parsing_error_listener import StopParsingListener
from typecheck_visitor import TypeCheckingVisitor
from verbose_error_listener import VerboseErrorListener
from virtual_machine import VirtualMachine


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
        else:
            print("Type Checking is Ok")
            print()
            output_visitor = OutputVisitor(
                typecheck_visitor.symbol_table, typecheck_visitor.context_dict
            )
            output = output_visitor.visit(tree)
            output_str = "\n".join(output)
            print("OutputVisitor:")
            print(output_str)

            with open("output.txt", "w") as file:
                file.write(output_str)

            # print("#" * 30)
            # print("VIRTUAL MACHINE")
            # vm = VirtualMachine("output.txt")
            # vm.run()


if __name__ == "__main__":
    main(sys.argv)