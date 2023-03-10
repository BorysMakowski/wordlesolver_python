import random

class Game:
    def __init__(self, word_list):
        self.word_list = word_list
        self.tries = 0
        self.finished = False
        self.result = False
        self.solution = random.choice(self.word_list)

    def guess(self, word):
        if not word in self.word_list:
            print("not a word")
            pass
        
        self.tries += 1

        output = ""
        for i in range(5):
            if word[i] == self.solution[i]:
                output += self.solution[i]
            else:
                if word[i] in self.solution:
                    output += "+"
                else:
                    output += "-"
        
        if output == word:
            self.finished = True
            self.result = True
            return output
        
        if self.tries < 6:
            return output
        else:
            self.finished = True
            self.result = False
            return "-----"

    def get_solution(self):
        return self.solution

    def is_finished(self) -> bool:
        return self.finished

    def is_won(self) -> bool:
        return self.result

    def get_word_list(self):
        return self.word_list