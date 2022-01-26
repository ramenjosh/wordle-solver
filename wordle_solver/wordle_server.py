# wordle_server.py
#
# Defines a server for playing the game wordle.
# Initialised with a single word, which is considered as being hidden to the client.
from dataclasses import dataclass
from wordle_solver.information import (
    Information,
    LetterNotPresent,
    LetterPresentCorrectPosition,
    LetterPresentIncorrectPosition,
    parse_information_string,
)

from typing import Optional, List


@dataclass
class KnownWordleServer:
    """
    Represents a Wordle Server with a known word.
    Can be used for local testing.
    """

    word: str

    def handler(self, guess: str) -> Optional[List[Information]]:
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

        result: List[Information] = []
        for index, char in enumerate(guess):
            if self.word[index] == char:
                result.append(LetterPresentCorrectPosition(letter=char, position=index))
            elif char in self.word:
                result.append(
                    LetterPresentIncorrectPosition(letter=char, position=index)
                )
            else:
                result.append(LetterNotPresent(letter=char))

        return result


@dataclass
class RemoteWordleServer:
    """
    Represents a remote wordle server where the word is unknown.
    Requires input from the user as to what the server responded with.

    This input is then converted into a List of Information.
    """

    def handler(self, guess: str) -> Optional[List[Information]]:
        """ """

        print(
            f"""Please input the following guess into your Wordle game:

*********
* {guess} *
*********
"""
        )

        while True:
            server_resp = input(
                """Please input the response from the server below.
Use '_' for incorrect letter, '?' for incorrect position and 'Y' for correct position:

"""
            )
            try:
                information = parse_information_string(guess=guess, instr=server_resp)
                return information
            except TypeError as err:
                print(err)
                print("Please try and input the server response again.")
