from wordle_solver.wordle_client import BasicWordleClient
from wordle_solver.information import (
    LetterNotPresent,
    LetterPresentCorrectPosition,
    LetterPresentIncorrectPosition,
)

test_word_list = [
    "above",
    "digit",
    "hiked",
    "pasta",
    "whack",
]


def test_letter_not_present_filtering():
    client = BasicWordleClient(word_list=test_word_list, information=[])
    information = [LetterNotPresent("a")]

    client.update_new_information(information)

    assert client.word_list == [
        "digit",
        "hiked",
    ]


def test_letter_present_incorrect_position_filtering():
    client = BasicWordleClient(word_list=test_word_list, information=[])
    information = [LetterPresentIncorrectPosition("a", 0)]

    client.update_new_information(information)

    assert client.word_list == [
        "pasta",
        "whack",
    ]


def test_letter_present_correct_position_filtering():
    client = BasicWordleClient(word_list=test_word_list, information=[])
    information = [LetterPresentCorrectPosition("a", 1)]

    client.update_new_information(information)

    assert client.word_list == [
        "pasta",
    ]
