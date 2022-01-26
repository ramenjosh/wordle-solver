from wordle_solver.wordle_client import IndexedWordleClient

# from wordle_solver.wordle_client import BasicWordleClient
# from wordle_solver.wordle_server import KnownWordleServer
from wordle_solver.wordle_server import RemoteWordleServer
from wordle_solver.words import WORDS

# from wordle_solver.information import information_list_to_str

if __name__ == "__main__":
    # server = KnownWordleServer("penis")
    server = RemoteWordleServer()

    # client = BasicWordleClient(word_list=WORDS, information=[])
    client = IndexedWordleClient(word_list=WORDS, information=[])
    print(f"There are {len(client.word_list)} possible words to choose from!")

    for turn in range(6):
        print(f"\n*********** Turn {turn} ***********")
        guess = client.pick_guess()
        if len(client.word_list) == 1:
            print(f"Figured it out! Word is '{guess}'")
            break

        new_info = server.handler(guess)
        # print(f"Server reponse: {information_list_to_str(new_info)}")
        if new_info:
            client.update_new_information(new_info)
            print(f"\nThere are now only {len(client.word_list)} possible words!")
