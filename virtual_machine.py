import shlex
import sys
from collections import deque
from typing import Any

from type_enum import Type


class VirtualMachine:
    def __init__(self, code_filepath: str):
        with open(code_filepath, "r") as file:
            self.instructions = file.read().split("\n")

        self.stack: deque[tuple[Type, Any]] = deque()
        self.instruction_pointer = 0
        self.variable_table: dict[str, tuple[Type, Any]] = {}
        self.jump_table: dict[int, int] = {}
        self.fill_jump_table()

    def fill_jump_table(self):
        for row, instruction in enumerate(self.instructions):
            if instruction.startswith("label"):
                self.jump_table[int(instruction.split(" ")[1])] = row

    def run(self):
        while self.instruction_pointer < len(self.instructions):
            instruction = self.instructions[self.instruction_pointer]
            match shlex.split(instruction):
                case _:
                    raise ValueError(
                        f"Invalid instruction [{self.instruction_pointer}]: {instruction}"
                    )

            self.instruction_pointer += 1


def main(argv):
    vm = VirtualMachine("output.txt")
    vm.run()


if __name__ == "__main__":
    main(sys.argv)
