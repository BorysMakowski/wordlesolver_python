import wordle_solver as ws


if __name__ == '__main__':
    word_list = ws.propagate_word_list()
    times_to_run = 10000;
    file = open("results.txt", "w")
    solver = ws.SolverMatchPatternA(word_list)
    ws.reduce_word_list(word_list, 3000)
    ws.test(solver, file, times_to_run, word_list, False)

    file.close()




