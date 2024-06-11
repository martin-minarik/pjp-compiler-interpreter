import sys
import tempfile

from src.compiler import get_arg_parser, compile_code
from src.virtual_machine import VirtualMachine


def main() -> None:
    arg_parser = get_arg_parser()
    args = arg_parser.parse_args()

    output_instructions = compile_code(args.input_file, args.verbose)
    if output_instructions:  # Compile
        # Save instructions
        if args.output_file_flag:
            with open(args.output_file, "w") as file:
                file.write(output_instructions)

        # Interpret instructions
        if args.interpret:
            with tempfile.NamedTemporaryFile(
                    mode="w", delete_on_close=False
            ) as temp_file:
                temp_file.write(output_instructions)
                temp_file.close()

                print("#" * 15)
                print("Virtual Machine:")
                vm = VirtualMachine(temp_file.name)
                vm.run()


if __name__ == "__main__":
    main()
