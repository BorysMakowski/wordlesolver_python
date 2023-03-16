import random
import solver
import time
from typing import List, Any
from game import Game

class SolverMatchPatternA(solver.Solver):
    def __init__(self, word_list):
        super().__init__(word_list)
        self.pattern = [[] for _ in range(5)]
        self.reduced_word_list = []
        self.required_letters=[]

    def solve(self, game: Game):
        self.required_letters = []

        self.reset_pattern()
        self.reduced_word_list = self.wordList
        self.wordListSizes[0] += len(self.reduced_word_list)
        rand_num = random.randint(0, len(self.reduced_word_list) - 1)
        prev_guess = self.reduced_word_list[rand_num]
        prev_result = game.guess(prev_guess)
        # print(prev_guess);
        # print(prev_result);
        guess_number = 1

        while not game.is_finished() and not game.is_won():
            for i in range(5):
                if prev_result[i] == '-':
                    self.remove_from_pattern(prev_guess[i])
                elif prev_result[i] == '+':
                    if prev_guess[i] not in self.required_letters:
                        self.required_letters.append(prev_guess[i])
                    if prev_guess[i] in self.pattern[i]:
                        self.pattern[i].remove(prev_guess[i])
                else:
                    self.pattern[i].clear()
                    self.pattern[i].append(prev_result[i])

            self.reduced_word_list = self.apply_pattern()

            self.wordListSizes[guess_number] += len(self.reduced_word_list)
            rand_num = random.randint(0, len(self.reduced_word_list) - 1)
            prev_guess = self.reduced_word_list[rand_num]
            # print("new size: ",len(self.reduced_word_list))
            prev_result = game.guess(prev_guess)
            guess_number += 1

            #self.show_pattern();
            # print("required letters: ", self.required_letters )
            # print(prev_guess);
            # print(prev_result);



        if game.is_won():
            self.timesWon += 1
            self.wonAtGuess[guess_number] += 1
        else:
            self.timesLost += 1

    def show_pattern(self):
            for sub_pattern in self.pattern:
                print(sub_pattern);

    def reset_pattern(self):
        self.pattern = [[] for _ in range(5)]
        for i in range(5):
            for j in range(97, 123):
                self.pattern[i].append(chr(j))

    def apply_pattern(self) -> List[Any]:
        output=[]
        for word in self.reduced_word_list:
            if self.matches_pattern(word) and self.contains_required_letters(word):
                output.append(word)
        return output

    def remove_from_pattern(self, letter):
        for sub_pattern in self.pattern:
            if letter in sub_pattern:
                sub_pattern.remove(letter)

    def matches_pattern(self,word):
        for i in range(5):
            if word[i] not in self.pattern[i]:
                return False
        return True

    def contains_required_letters(self,word):
        for required_letter in self.required_letters:
            if required_letter not in word:
                return False
        return True

