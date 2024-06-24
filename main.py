from E_graphs_find_judge import findJudge
from E_graphs_find_path import findPath
from E_graphs_find_center_star_graph import findCenter
from M_graphs_course_scedule import canFinishCourses

def __main__():
    findJudge(2, [[1, 2]])
    findJudge(3, [[1, 3], [2, 3]])
    findJudge(3, [[1, 3], [2, 3], [3, 1]])
    findJudge(3, [[1, 2], [2, 3]])
    findJudge(4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]])
    print("\n")

    findPath(8, [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [6, 7]], 0, 7)
    findPath(8, [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [6, 7]], 0, 7, is_bidirectional=False)
    print("\n")

    findCenter([[1,2],[5,1],[1,3],[1,4]])
    print("\n")

    canFinishCourses(2, [[0, 1], [1, 0]])
    #canFinishCourses(3, [[1, 0], [1, 2], [2, 1]])
    canFinishCourses(4, [[1, 0], [1, 2], [2, 0], [3, 2], [1, 3]])
    canFinishCourses(4, [[1, 0], [1, 2], [2, 0], [3, 2], [1, 3], [3, 1]])

__main__()