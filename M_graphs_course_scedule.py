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
import collections

def canFinishCourses(numCourses, prerequisits):
	graph = collections.defaultdict(list)
	
	for course, prereq in prerequisits:
		graph[course].append(prereq)
	
	inProcess = []
	queue = []
	for node in range(numCourses):
		if graph[node]:
			inProcess.append(node)
			queue.append(graph[node].pop())
		
		while queue:
			node = queue.pop()
			if node in inProcess:
				print(f"Cycle found in {prerequisits}. Cannot finish courses.")
				return False
			
			if graph[node]:
				inProcess.append(node)
				queue.append(graph[node].pop())
	
	print(f"Cycle NOT found in {prerequisits}. Can finish courses.")
	return True



def canFinishCoursesRecursive(numCourses, prerequisists):
	graph = collections.defaultdict(list)

	for course, prereq in prerequisists:
		graph[course].append(prereq)
		
	for course in graph.keys():
		tracker = {}
		if dfsCyclic(course, graph, tracker):
			print("Cycle found. Cannot finish courses.")
			return False
		
	print("Cycle NOT found. Can finish courses.")
	return True
	
def dfsCyclic(course, graph, tracker):
	tracker[course] = True
	
	for n in graph[course]:
		if n in tracker or dfsCyclic(n, graph, tracker):
			return True
	
	tracker.pop(course)
	return False