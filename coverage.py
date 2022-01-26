from wordle_solver.wordle_client import IndexedWordleClient

# from wordle_solver.wordle_client import BasicWordleClient
from wordle_solver.wordle_server import WordleServer
from wordle_solver.words import WORDS


def did_guess_within_n_turns(client, server: WordleServer, n: int) -> bool:
    for turn in range(n):
        guess = client.pick_guess()
        if len(client.word_list) == 1:
            print(f"Guessed {guess} in {turn+1} turns!")
            return True
        new_info = server.handler(guess)
        client.update_new_information(new_info)
    # print("Failed to guess word")
    return False


if __name__ == "__main__":
    correct = 0
    total = len(WORDS)
    n = 6
    for word in WORDS:
        client = IndexedWordleClient(word_list=WORDS, information=[])
        server = WordleServer(word)
        if did_guess_within_n_turns(client, server, n):
            correct += 1

    print(f"Guessed {correct} / {total} within {n} turns.")
