from src.virtual_machine import VirtualMachine, get_arg_parser


def main():
    arg_parser = get_arg_parser()
    args = arg_parser.parse_args()

    vm = VirtualMachine(args.input_file)
    vm.run()


if __name__ == "__main__":
    main()
