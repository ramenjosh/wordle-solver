from dataclasses import dataclass
from typing import Union, Optional, List


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


def information_list_to_str(inlist: Optional[List[Information]]) -> Optional[str]:
    if inlist is None:
        return None
    else:
        return "".join(map(str, inlist))


def parse_information_string(guess: str, instr: str) -> List[Information]:
    """
    Returns a List of Information based on a provided string.
    """
    information: List[Information] = []
    for ind, (c, r) in enumerate(zip(guess, instr)):
        if r == "_":
            information.append(LetterNotPresent(letter=c))
        elif r == "?":
            information.append(LetterPresentIncorrectPosition(letter=c, position=ind))
        elif r == "Y":
            information.append(LetterPresentCorrectPosition(letter=c, position=ind))
        else:
            raise TypeError(f"Unable to parse character {c} in input.")

    return information
