from typing import Any

from antlr4.Token import Token

from errors import Errors
from type_enum import Type


class SymbolTable:
    def __init__(self):
        self.memory: dict[str, tuple[Type, Any]] = {}

    def add(self, variable: Token, type_: Type) -> None:
        name = variable.text.strip()
        if name in self.memory:
            Errors.report_error(variable, f"Variable {name} was already declared.")
        else:
            self.memory[name] = (type_, 0 if type_ == Type.Int else 0.0)

    def __getitem__(self, variable: Token) -> tuple[Type, Any]:
        name = variable.text.strip()
        if name in self.memory:
            return self.memory[name]
        else:
            Errors.report_error(variable, f"Variable {name} was NOT declared.")
            return Type.Error, 0

    def __setitem__(self, variable: Token, value: Any) -> None:
        name = variable.text.strip()
        self.memory[name] = value
