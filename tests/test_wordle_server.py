from wordle_solver.wordle_server import WordleServer
from wordle_solver.information import Information

from typing import Optional, List


def information_list_to_str(inlist: Optional[List[Information]]) -> Optional[str]:
    if inlist is None:
        return None
    else:
        return "".join(map(str, inlist))


def test_server_two_letters():
    server = WordleServer("opera")
    guess = "there"

    assert information_list_to_str(server.handler(guess)) == "__YY?"


def test_server_no_letters():
    server = WordleServer("opera")
    guess = "jjjjj"

    assert information_list_to_str(server.handler(guess)) == "_____"


def test_server_short_guess():
    server = WordleServer("opera")
    guess = "a"

    assert information_list_to_str(server.handler(guess)) is None


def test_server_long_guess():
    server = WordleServer("opera")
    guess = "abcdefgh"

    assert information_list_to_str(server.handler(guess)) is None
