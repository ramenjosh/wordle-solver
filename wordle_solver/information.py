from dataclasses import dataclass
from typing import Union


@dataclass
class LetterNotPresent:
    letter: str

    def __str__(self) -> str:
        return "_"

    def __post_init__(self):
        if len(self.letter) != 1:
            raise TypeError("Letter must be a single character.")


@dataclass
class LetterPresentIncorrectPosition:
    letter: str
    position: int

    def __str__(self) -> str:
        return "?"

    def __post_init__(self):
        if len(self.letter) != 1:
            raise TypeError("Letter must be a single character.")


@dataclass
class LetterPresentCorrectPosition:
    letter: str
    position: int

    def __str__(self) -> str:
        return "Y"

    def __post_init__(self):
        if len(self.letter) != 1:
            raise TypeError("Letter must be a single character.")


Information = Union[
    LetterNotPresent, LetterPresentIncorrectPosition, LetterPresentCorrectPosition
]
