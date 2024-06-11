import argparse
import os
from typing import Optional

from antlr4 import *

from .errors import Errors
from .language.LanguageLexer import LanguageLexer
from .language.LanguageParser import LanguageParser
from .output_visitor import OutputVisitor
from .typecheck_visitor import TypeCheckingVisitor


def compile_code(input_filepath: str, verbose=False) -> Optional[str]:
    input_stream = FileStream(input_filepath)
    lexer = LanguageLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = LanguageParser(stream)
    tree = parser.program()

    if parser.getNumberOfSyntaxErrors() > 0:
        print("syntax errors")
    else:
        if verbose:
            print("Grammar is Ok")

        typecheck_visitor = TypeCheckingVisitor()
        typecheck_visitor.visit(tree)

        if Errors.number_of_errors():
            Errors.print_and_clear_errors()
            return
        else:
            if verbose:
                print("Type Checking is Ok")

            output_visitor = OutputVisitor(
                typecheck_visitor.symbol_table, typecheck_visitor.context_dict
            )
            output = output_visitor.visit(tree)
            output_str = "\n".join(output)

            return output_str


def get_arg_parser():
    arg_parser = argparse.ArgumentParser()

    arg_parser.add_argument("input_file", type=str, help="Input file path")
    arg_parser.add_argument(
        "-o",
        "--output_file",
        type=str,
        default=os.path.join(os.getcwd(), "output_instructions.txt"),
    )
    arg_parser.add_argument(
        "--no_output_file", dest="output_file_flag", action="store_false"
    )
    arg_parser.add_argument("-v", "--verbose", action="store_true")

    arg_parser.add_argument("-i", "--interpret", action="store_true")

    return arg_parser
