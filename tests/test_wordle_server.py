from wordle_solver.wordle_server import WordleServer


def test_server_two_letters():
    server = WordleServer("opera")
    guess = "there"

    assert server.handler(guess) == "__YY?"


def test_server_no_letters():
    server = WordleServer("opera")
    guess = "jjjjj"

    assert server.handler(guess) == "_____"


def test_server_short_guess():
    server = WordleServer("opera")
    guess = "a"

    assert server.handler(guess) is None


def test_server_long_guess():
    server = WordleServer("opera")
    guess = "abcdefgh"

    assert server.handler(guess) is None
