# wordle_client.py
#
# Defines a client that can be used to play the game of wordle

from wordle_solver.information import Information
from dataclasses import dataclass
from typing import List


@dataclass
class BasicWordleClient:
    """
    Most simple wordle client I could think of.

    Makes a random guess, filters the word list by information.
    """

    information: List[Information]
    word_list: List[str]

    def pick_guess(self) -> str:
        return self.word_list[0]

    def update_new_information(self, information: List[Information]) -> None:
        new_word_list = list(
            filter(lambda s: all(i.filter(s) for i in information), self.word_list)
        )
        self.word_list = new_word_list
