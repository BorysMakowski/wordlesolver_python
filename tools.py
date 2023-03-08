import random
def propagate_word_list():
    word_list = []
    with open("words_alpha.txt") as word_file:
        for line in word_file:
            temp = line.strip()
            if len(temp) == 5:
                word_list.append(temp)
    return word_list

def play(word_list):
    temp = ""
    game = game.Game(word_list)
    while not game.is_finished():
        temp = input()
        print(game.guess(temp))
    if game.is_won():
        print("You won!")
    else:
        print("You lost!")

    #print(game.get_solution())

def reduce_word_list(wordlist,finalSize):
    if len(wordlist) > finalSize and finalSize > 5:
        while len(wordlist)>finalSize:
            wordlist.pop(random.randrange(len(wordlist)))