def bellman_ford(Alist, start):
    visited, distance = {}, {}
    infinity = float('inf')
    for key in Alist.keys():
        visited[key] = False
        distance[key] = infinity

    distance[start] = 0
    n = len(Alist.keys())
    for i in range(n):
        for u in Alist.keys():
            for v, d in Alist[u]:
                if distance[u] + d < distance[v]:
                    distance[v] = distance[u] + d
            visited[u] = True
    return distance


# Sample adjacency list for testing with a negative edge weight
sample_graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('C', -1), ('D', 2)],
    'C': [('D', 3), ('E', 2)],
    'D': [('E', -5)],
    'E': []
}

if __name__ == "__main__":
    print(bellman_ford(sample_graph, 'A'))
