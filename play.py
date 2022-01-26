from wordle_solver.wordle_client import IndexedWordleClient

# from wordle_solver.wordle_client import BasicWordleClient
from wordle_solver.wordle_server import WordleServer
from wordle_solver.words import WORDS
from wordle_solver.information import information_list_to_str

if __name__ == "__main__":
    server = WordleServer("penis")

    # client = BasicWordleClient(word_list=WORDS, information=[])
    client = IndexedWordleClient(word_list=WORDS, information=[])
    print(f"Starting word list length: {len(client.word_list)}")

    for turn in range(20):
        print(f"Turn {turn}")
        guess = client.pick_guess()
        if len(client.word_list) == 1:
            print(f"Figured it out! Word is '{guess}'")
            break
        else:
            print(f"Guessing: {guess}")

        new_info = server.handler(guess)
        print(f"Server reponse: {information_list_to_str(new_info)}")
        if new_info:
            client.update_new_information(new_info)
            print(f"New word list length: {len(client.word_list)}")
