"""
Dijkstra's algorithm finds the shortest path from a starting node to all other nodes
in a weighted graph, as long as all edge weights are non-negative.

How it works:
1. Set the distance of the start node to 0 and all others to infinity.
2. Mark all nodes as unvisited.
3. Pick the unvisited node with the smallest current distance.
4. For each neighbor of that node, relax the edge if a shorter path is found.
5. Repeat until all nodes have been processed.

Example idea:
A -> C (2) -> D (8) -> E (10)
A -> B (4) -> C (1) -> D (5) -> E (2)

Visualization:
A --2-- C --8-- D --2-- E
 \      |\
  \     | \ 
   4    1  5
    \   |  /
     B ----

In this example, the shortest path from A to B is A -> C -> B with total cost 3.
"""


def djikstra_SSP(Alist, v):
    infinity = float('inf')
    visited, distance = {}, {}
    for key in Alist.keys():
        visited[key], distance[key] = False, infinity
    distance[v] = 0

    for k in Alist.keys():
        min_distance = min([distance[k]
                           for k in Alist.keys() if not visited[k]])
        min_vertices = [k for k in Alist.keys() if (
            not visited[k] and distance[k] == min_distance)]
        next_vertex = min(min_vertices)
        visited[next_vertex] = True

        for vertex, d in Alist[next_vertex]:
            if not visited[vertex]:
                if distance[next_vertex] + d < distance[vertex]:
                    distance[vertex] = distance[next_vertex]+d

    return distance


# Sample adjacency list for testing
sample_graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('C', 1), ('D', 5)],
    'C': [('B', 1), ('D', 8), ('E', 10)],
    'D': [('E', 2)],
    'E': []
}

if __name__ == "__main__":
    print(djikstra_SSP(sample_graph, 'A'))
