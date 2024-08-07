from E_graphs_find_judge import findJudge
from E_graphs_find_path import findPath
from E_graphs_find_center_star_graph import findCenter
from M_graphs_course_schedule import canFinishCourses, canFinishCoursesRecursive
from M_graphs_course_schedule_ii import findCourseOrder, findCourseOrderRecursive
from delete_nodes_return_forest import Solution

def __main__():
    findJudge(2, [[1, 2]])
    findJudge(3, [[1, 3], [2, 3]])
    findJudge(3, [[1, 3], [2, 3], [3, 1]])
    findJudge(3, [[1, 2], [2, 3]])
    findJudge(4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]])

    print("\n\n")

    findPath(8, [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [6, 7]], 0, 7)
    findPath(8, [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [6, 7]], 0, 7, is_bidirectional=False)

    print("\n\n")

    findCenter([[1,2],[5,1],[1,3],[1,4]])

    print("\n\n")

    canFinishCourses(2, [[0, 1], [1, 0]])
    canFinishCourses(3, [[1, 0], [1, 2], [2, 1]])
    canFinishCourses(4, [[1, 0], [1, 2], [2, 0], [3, 2], [1, 3]])
    canFinishCourses(4, [[1, 0], [1, 2], [2, 0], [3, 2], [1, 3], [3, 1]])

    print("\n\n")

    ## not working
    #canFinishCoursesRecursive(2, [[0, 1], [1, 0]])
    #canFinishCoursesRecursive(3, [[1, 0], [1, 2], [2, 1]])
    #canFinishCoursesRecursive(4, [[1, 0], [1, 2], [2, 0], [3, 2], [1, 3]])
    #canFinishCoursesRecursive(4, [[1, 0], [1, 2], [2, 0], [3, 2], [1, 3], [3, 1]])
    #print("\n\n")

    findCourseOrder(2, [[1, 0]])
    findCourseOrder(4, [[1,0],[2,0],[3,1],[3,2]])
    findCourseOrder(4, [[1,0],[1,3], [2,0],[3,1],[3,2]])

    print("\n\n")

    findCourseOrderRecursive (2, [[1, 0]])
    findCourseOrderRecursive(4, [[1,0],[2,0],[3,1],[3,2]])
    findCourseOrderRecursive(4, [[1,0],[1,3], [2,0],[3,1],[3,2]])

    solution = Solution()
    solution.delNodes(None, [1, 2])



__main__()