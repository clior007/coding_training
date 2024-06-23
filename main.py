from graphs_find_judge import findJudge
from graphs_find_path import find_path

def __main__():
    findJudge(2, [[1, 2]])
    findJudge(3, [[1, 3], [2, 3]])
    findJudge(3, [[1, 3], [2, 3], [3, 1]])
    findJudge(3, [[1, 2], [2, 3]])
    findJudge(4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]])

    find_path(3, [[0, 1], [1, 2], [2, 0]], 0, 2)

__main__()