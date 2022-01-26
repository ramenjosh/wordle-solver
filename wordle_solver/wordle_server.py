# wordle_server.py
#
# Defines a server for playing the game wordle.
# Initialised with a single word, which is considered as being hidden to the client.
from dataclasses import dataclass

from typing import Optional


@dataclass
class WordleServer:

    word: str

    def handler(self, guess: str) -> Optional[str]:
        """
        Given a client's guess, returns a string where each character contains the
        following information:

        '_' denotes that a character was not used in the word.
        '?' denotes that a character was used in the word, but not at this location.
        'Y' denotes that a character was used in the word, at this location.

        Guesses that do not contain the same number of characters as the word are
        considered invalid, and will return None.
        """

        if len(guess) != len(self.word):
            return None

        result = ""
        for index, char in enumerate(guess):
            if self.word[index] == char:
                result += "Y"
            elif char in self.word:
                result += "?"
            else:
                result += "_"

        return result
