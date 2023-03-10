from abc import ABC, abstractmethod

class Solver(ABC):
    def __init__(self, word_list):
        self.wordList = word_list
        self.timesWon = 0
        self.timesLost = 0
        self.wordListSizes = [0, 0, 0, 0, 0, 0]
        self.wonAtGuess = [0, 0, 0, 0, 0, 0, 0]

    @abstractmethod
    def solve(self, game):
        pass

    def get_times_won(self):
        return self.timesWon

    def get_times_lost(self):
        return self.timesLost

    def get_word_list_sizes(self):
        return self.wordListSizes

    def get_won_at_guess(self):
        return self.wonAtGuess