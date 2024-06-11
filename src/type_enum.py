from enum import Enum, auto


class Type(Enum):
    Int = auto()
    Float = auto()
    Bool = auto()
    String = auto()
    Error = auto()

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
