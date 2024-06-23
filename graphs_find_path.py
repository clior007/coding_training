# Given an undirected graph, find a path between two nodes.
# For example, given the following graph:
# n=3, edges = [[0, 1], [1, 2], [2, 0]], source = 0, and destination = 2, the function should return true.

def find_path(n, edges, source, destination):
    graph = {}

    # Build the graph based on the edges
    for u, v in edges:
        if u not in graph:
            graph[u] = []
        graph[u].append(v)
        
        if v not in graph:
            graph[v] = []
        graph[v].append(u)
    print("Graph: ", graph)

    # find a path from source to dest in the graph
    visited = [False] * n
    return dfs(graph, source, destination, visited)

def dfs(graph, source, destination, visited):
    print(f"Trying to find a path from source {source} to destination {destination}")
    print("Visited: ", visited)
    for u in graph[source]:
        if u == destination:
            print(f"There is a path between {source} and {destination}")
            return True
        if visited[u]:
            return False
        visited[u] = True
        
        if dfs(graph, u, destination, visited):
            return True
