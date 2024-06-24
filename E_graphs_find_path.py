# Given an undirected graph, find a path between two nodes.
# For example, given the following graph:
# n=8, edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [6, 7]], source = 0, and destination = 7, the function should return true.

def findPath(n, edges, source, destination, is_bidirectional=True):
    graph = {}

    for i in range(n):
        graph[i] = []

    # Build the graph based on the edges
    for u, v in edges:
        graph[u].append(v)
        
        if is_bidirectional:
            graph[v].append(u)
    print("Graph: ", graph)

    # find a path from source to dest in the graph
    visited = [False] * n
    if bfs(graph, visited, source, destination):
        print(f"BFS: There is a path between {source} and {destination}")
    else:
        print(f"BFS: There is NO path between {source} and {destination}")

    visited = [False] * n
    if dfs(graph, visited, source, destination):
        print(f"DFS: There is a path between {source} and {destination}")
    else:
        print(f"DFS: There is NO path between {source} and {destination}")

def bfs(graph, visited, source, destination):
    queue = []
    queue.append(source)
    visited[source] = True
    
    while queue:
        print(f"B-FS: queue: {queue}, visited: {visited}")
        u = queue.pop(0)
        if u == destination:
            return True
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                queue.append(v)
    return False

def dfs(graph, visited, source, destination):
    queue = []
    queue.append(source)
    visited[source] = True

    while queue:
        print(f"D-FS: queue: {queue}, visited: {visited}")
        u = queue.pop()
        if u == destination:
            return True
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                queue.append(v)

    return False