from typing import List
from game import Game
from abc import ABC, abstractmethod

class Solver(ABC):
    def __init__(self, word_list):
        self.wordList = word_list
        self.timesWon = 0
        self.timesLost = 0
        self.wordListSizes = [0, 0, 0, 0, 0, 0]
        self.wonAtGuess = [0, 0, 0, 0, 0, 0, 0]

    @abstractmethod
    def solve(self, game: Game):
        pass

    def get_times_won(self) -> int:
        return self.timesWon

    def get_times_lost(self) -> int:
        return self.timesLost

    def get_word_list_sizes(self) -> List[int]:
        return self.wordListSizes

    def get_won_at_guess(self) -> List[int]:
        return self.wonAtGuess