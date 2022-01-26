# wordle_client.py
#
# Defines a client that can be used to play the game of wordle

from wordle_solver.information import Information
from dataclasses import dataclass
from typing import Counter, List, Set


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


@dataclass
class IndexedWordleClient:
    """
    Slightly more complex client.

    Builds an index of occurrences of letters in the word list that we don't
    have information about.

    Picks guesses based on words containing the most popular letters.
    """

    information: List[Information]
    word_list: List[str]

    def pick_guess(self) -> str:
        letters_with_information = {i.letter for i in self.information}

        index: Counter = Counter()
        for w in self.word_list:
            for c in w:
                if c not in letters_with_information:
                    index[c] += 1

        scored_words = sorted(
            self.word_list,
            key=lambda w: score_word_no_duplicates(w, index),
            reverse=True,
        )
        return scored_words[0]

    def update_new_information(self, information: List[Information]) -> None:
        new_word_list = list(
            filter(lambda s: all(i.filter(s) for i in information), self.word_list)
        )
        self.word_list = new_word_list


def score_word_no_duplicates(word: str, index: Counter) -> int:
    seen: Set[str] = set()
    score = 0

    for c in word:
        if c not in seen:
            score += index[c]
            seen.add(c)

    return score
