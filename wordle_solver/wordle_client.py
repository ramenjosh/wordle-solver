# wordle_client.py
#
# Defines a client that can be used to play the game of wordle

from dataclasses import dataclass
from typing import List


@dataclass
class GameStep:

    information: List
