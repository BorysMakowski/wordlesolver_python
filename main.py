import solver_match_pattern_a as smpa
import game as g
import time

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






if __name__ == '__main__':
    word_list = propagate_word_list()
    times_to_run = 100;
    start = time.perf_counter()
    solver = smpa.SolverMatchPatternA(word_list)

    for i in range(times_to_run):
        #print(i)
        game = g.Game(word_list)
        print(game.get_solution())
        solver.solve(game)

    end = time.perf_counter()
    time_elapsed = end - start
    print("won:")
    print(solver.get_times_won())
    print("lost:")
    print(solver.get_times_lost())
    print("job took:")
    print(time_elapsed)

    for i, wins in enumerate(solver.wonAtGuess):
        print("won at ", i, " ", wins)

    f = open("results_python.txt", "w")
    f.write("solver match pattern a - python implementation\n")
    f.write("num of attempts: " + str(times_to_run) + "\n")
    f.write("won games: " + str(solver.get_times_won()) + "\n")
    f.write("lost games: " + str(solver.get_times_lost()) + "\n")
    f.write("job took/: " + str(time_elapsed) + " seconds\n")
    for i, size in enumerate(solver.wordListSizes):
        f.write("mean Wordlist size after attempt " + str(i) + ": " + str(size/times_to_run) + "\n")
    for i, win_num in enumerate(solver.wonAtGuess):
        f.write("Won at guess " + str(i) + ": " + str(win_num) + "\n")
    f.close()


