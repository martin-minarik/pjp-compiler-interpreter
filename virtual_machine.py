import argparse
import os
import shlex
import sys
from collections import deque
from typing import Any

from type_enum import Type


class VirtualMachine:
    def __init__(self, code_filepath: str):
        with open(code_filepath, "r") as file:
            self.instructions = file.read().split("\n")

        self.instruction_pointer = 0
        self.stack: deque[tuple[Type, Any]] = deque()
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
                case ["push", type_, literal]:
                    self.push_instruction(type_, literal)

                case ["print", number]:
                    self.print_instruction(number)

                case ["read", type_]:
                    self.read_instruction(type_)

                case ["save", variable]:
                    self.save_instruction(variable)

                case ["load", variable]:
                    self.load_instruction(variable)

                case ["pop"]:
                    self.pop_instruction()

                case ["uminus"]:
                    self.uminus_instruction()

                case ["itof"]:
                    self.itof_instruction()

                case ["mul"]:
                    self.mul_instruction()

                case ["div"]:
                    self.div_instruction()

                case ["mod"]:
                    self.mod_instruction()

                case ["add"]:
                    self.add_instruction()

                case ["sub"]:
                    self.sub_instruction()

                case ["concat"]:
                    self.concat_instruction()

                case ["lt"]:
                    self.lt_instruction()

                case ["gt"]:
                    self.gt_instruction()

                case ["and"]:
                    self.and_instruction()

                case ["or"]:
                    self.or_instruction()

                case ["eq"]:
                    self.eq_instruction()

                case ["not"]:
                    self.not_instruction()

                case ["label", label_id]:
                    pass

                case ["fjmp", label_id]:
                    if not self.stack.popleft()[1]:
                        self.instruction_pointer = self.jump_table[int(label_id)]

                case ["jmp", label_id]:
                    self.instruction_pointer = self.jump_table[int(label_id)]

                case _:
                    raise ValueError(
                        f"Invalid instruction [{self.instruction_pointer}]: {instruction}"
                    )

            self.instruction_pointer += 1

    def push_to_stack(self, type_: str, value: str):
        match type_:
            case "I":
                self.stack.appendleft((Type.Int, int(value)))
            case "F":
                self.stack.appendleft((Type.Float, float(value)))
            case "B":
                self.stack.appendleft((Type.Bool, value == "true"))
            case "S":
                self.stack.appendleft((Type.String, value))
            case _:
                raise ValueError(f"Invalid type [{self.instruction_pointer}]")

    def push_instruction(self, type_: str, literal: str):
        self.push_to_stack(type_, literal)

    def print_instruction(self, number: str):
        buffer = []
        for n in range(int(number)):
            type_, value = self.stack.popleft()
            if type_ == Type.Float:
                value = round(value, 2)

            buffer.append(value)

        print(*buffer[::-1])

    def read_instruction(self, type_: str):
        input_ = input(f"Enter({type_}):")
        self.push_to_stack(type_, input_)

    def save_instruction(self, variable: str):
        self.variable_table[variable] = self.stack.popleft()

    def load_instruction(self, variable: str):
        self.stack.appendleft(self.variable_table[variable])

    def pop_instruction(self):
        self.stack.popleft()

    def uminus_instruction(self):
        item = self.stack[0]
        self.stack[0] = (item[0], -item[1])

    def mul_instruction(self):
        right, left = self.stack.popleft(), self.stack.popleft()
        self.stack.appendleft((left[0], left[1] * right[1]))

    def div_instruction(self):
        right, left = self.stack.popleft(), self.stack.popleft()
        if left[0] == Type.Int:
            self.stack.appendleft((left[0], left[1] // right[1]))
        else:
            self.stack.appendleft((left[0], left[1] / right[1]))

    def mod_instruction(self):
        right, left = self.stack.popleft(), self.stack.popleft()
        self.stack.appendleft((Type.Int, left[1] % right[1]))

    def add_instruction(self):
        right, left = self.stack.popleft(), self.stack.popleft()
        self.stack.appendleft((left[0], left[1] + right[1]))

    def sub_instruction(self):
        right, left = self.stack.popleft(), self.stack.popleft()
        self.stack.appendleft((left[0], left[1] - right[1]))

    def concat_instruction(self):
        right, left = self.stack.popleft(), self.stack.popleft()
        self.stack.appendleft((Type.String, left[1] + right[1]))

    def itof_instruction(self):
        self.stack[0] = (Type.Float, float(self.stack[0][1]))

    def lt_instruction(self):
        right, left = self.stack.popleft(), self.stack.popleft()
        self.stack.appendleft((Type.Bool, left[1] < right[1]))

    def gt_instruction(self):
        right, left = self.stack.popleft(), self.stack.popleft()
        self.stack.appendleft((Type.Bool, left[1] > right[1]))

    def and_instruction(self):
        right, left = self.stack.popleft(), self.stack.popleft()
        self.stack.appendleft((Type.Bool, left[1] and right[1]))

    def or_instruction(self):
        right, left = self.stack.popleft(), self.stack.popleft()
        self.stack.appendleft((Type.Bool, left[1] or right[1]))

    def eq_instruction(self):
        right, left = self.stack.popleft(), self.stack.popleft()
        self.stack.appendleft((Type.Bool, left[1] == right[1]))

    def not_instruction(self):
        item = self.stack.popleft()
        self.stack.appendleft((Type.Bool, not item[1]))


def get_arg_parser():
    arg_parser = argparse.ArgumentParser()

    arg_parser.add_argument('input_file', nargs="?", help='Input file path',
                            default=os.path.join(os.getcwd(), "output_instructions.txt"))

    return arg_parser


def main():
    arg_parser = get_arg_parser()
    args = arg_parser.parse_args()

    vm = VirtualMachine(args.input_file)
    vm.run()


if __name__ == "__main__":
    main()
