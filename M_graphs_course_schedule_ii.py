# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
# 
# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.
# 
#  
# 
# Example 1:
# 
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
# Example 2:
# 
# Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
# So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
# Example 3:
# 
# Input: numCourses = 1, prerequisites = []
# Output: [0]
#  
# 
# Constraints:
# 
# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= numCourses * (numCourses - 1)
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# ai != bi
# All the pairs [ai, bi] are distinct.


import collections

def findCourseOrder(numCourses, prerequisits):
	graph = collections.defaultdict(list)
	
	# build the graph of dependency
	for course, prereq in prerequisits:
		graph[course].append(prereq)
	
	inProcess = []
	queue = []
	order = []
	
	for course in range(numCourses):
		if graph[course]:
			inProcess.append(course)
			queue.append(graph[course].pop())
			
		while queue:
			node = queue.pop()
			for n in graph[node]:
				if n in inProcess:
					print(f"Cycle found in {prerequisits}. Cannot finish courses.")
					return False, []
				
			if graph[course]:
				queue.append(graph[course].pop())
		
		order.append(course)
		inProcess = []
	
	print(f"Can finish courses with the following order: {order}")
	return True, order

def findCourseOrderRecursive(numCourses, prerequisits):
    # build the graph
    graph = { c : [] for c in range(numCourses) }
    
    for c, prereq in prerequisits:
        graph[c].append(prereq)
        
    order = []
    visit = set()
    cycle = set()
    
    def dfsIsCycle(c):
        if c in visit:
            return False
        
        cycle.add(c)
        for n in graph[c]:
            if n in cycle or dfsIsCycle(n):
                print(f"Cycle found in {prerequisits}. Cannot finish courses.")
                return True
        
        cycle.remove(c)     
        visit.add(c)
        order.append(c)
        return False
        
    for course in range(numCourses):
        if dfsIsCycle(course) == True:
            return []
    
    print(f"Can finish courses with the following order: {order}")
    return order