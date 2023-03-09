import solver_match_pattern_a as smpa
import game as g
import random
import time

def test(file, times_to_run, word_list, print_to_console = True):

    start = time.perf_counter()
    solver = smpa.SolverMatchPatternA(word_list)

    for i in range(times_to_run):
        if print_to_console is True:
            print(i)
        game = g.Game(word_list)
        solver.solve(game)

    end = time.perf_counter()
    time_elapsed = end - start

    
    file.write("solver match pattern a - python implementation\n")
    file.write("num of attempts: " + str(times_to_run) + "\n")
    file.write("won games: " + str(solver.get_times_won()) + "\n")
    file.write("lost games: " + str(solver.get_times_lost()) + "\n")
    file.write("job took: " + str(time_elapsed) + " seconds\n")
    for i, size in enumerate(solver.wordListSizes):
        file.write("mean Wordlist size after attempt " + str(i) + ": " + str(size/times_to_run) + "\n")
    for i, win_num in enumerate(solver.wonAtGuess):
        file.write("Won at guess " + str(i) + ": " + str(win_num) + "\n")

def reduce_word_list(wordlist,finalSize):
    if len(wordlist) > finalSize and finalSize > 5:
        while len(wordlist)>finalSize:
            wordlist.pop(random.randrange(len(wordlist)))

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
    print(game.get_solution())