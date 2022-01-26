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

    def filter(self, s: str) -> bool:
        """
        Filters out words that have this letter within them.
        """
        return not (self.letter in s)


@dataclass
class LetterPresentIncorrectPosition:
    letter: str
    position: int

    def __str__(self) -> str:
        return "?"

    def __post_init__(self):
        if len(self.letter) != 1:
            raise TypeError("Letter must be a single character.")

    def filter(self, s: str) -> bool:
        """
        Filters out words that have this letter at the position indicated.
        """
        return (self.letter in s) and not (s[self.position] == self.letter)


@dataclass
class LetterPresentCorrectPosition:
    letter: str
    position: int

    def __str__(self) -> str:
        return "Y"

    def __post_init__(self):
        if len(self.letter) != 1:
            raise TypeError("Letter must be a single character.")

    def filter(self, s: str) -> bool:
        """
        Filters out words that have this letter at the position indicated.
        """
        return s[self.position] == self.letter


Information = Union[
    LetterNotPresent, LetterPresentIncorrectPosition, LetterPresentCorrectPosition
]
