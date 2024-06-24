# Course schedule
# There are a total of n courses you have to take, labeled from 0 to n-1.
# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
#
# Example 1:
# Input: 2, [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.
#
# Example 2:
# Input: 2, [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
#
# Note:
# The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
# You may assume that there are no duplicate edges in the input prerequisites.

def canFinishCourse(numCourses, prerequisits):
    graph = {}
    for i in range(numCourses):
        graph[i] = []

    for u_course, v_prereq in prerequisits:
        graph[u_course].append(v_prereq)

    print(f"course graph: {graph}")
    visited = [False] * numCourses

    result = dfs(graph, visited)
    print(f"Can finish courses: {result}")

def dfs(graph, visited):
    queue = []

    for ver_key in graph:
        if graph[ver_key] != []:
            queue.append(ver_key)
            break
        
    while queue:
        u = queue.pop()
        if visited[u] == 1:
            continue
        visited[u] = True

        for v in graph[u]:
            queue.append(v)

    return all(visited)

    