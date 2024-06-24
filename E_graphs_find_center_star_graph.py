# Find Center of Star Graph
# In a star graph, there is one center node and exactly N - 1 edges that connect the center node to N - 1 other nodes.
# You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that there is an edge between the nodes ui and vi.
# Return the center of the given star graph.

# Example 1:
# Input: edges = [[1,2],[2,3],[4,2]]
# Output: 2
# Explanation: As shown in the figure above, node 2 is connected to every other node, so 2 is the center.

# Example 2:
# Input: edges = [[1,2],[5,1],[1,3],[1,4]]
# Output: 1

# Constraints:
# 3 <= edges.length <= 105
# edges[i].length == 2
# 1 <= ui, vi <= n
# ui != vi
# The given edges represent a valid star graph.

def findCenter(edges):
    graph = {}

    for vert1, vert2 in edges:
        if vert1 not in graph:
            graph[vert1] = 0
        graph[vert1] += 1

        if vert2 not in graph:
            graph[vert2] = 0
        graph[vert2] += 1

    num_of_verts = graph.keys()
    for key in num_of_verts:
        if graph[key] == len(num_of_verts) - 1:
            print(f"The center of the star graph is: {key}")
            return key

