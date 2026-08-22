def prim_MST(WList):
    # Remember that this algorithm only works for connected graphs and that the edges must have weights
    infinity = float('inf')
    visited, distance, edge_in_MST = {}, {}, {}
    for key in WList.keys():
        visited[key], distance[key], edge_in_MST[key] = False, infinity, -1
    # can choose any vertex as the starting vertex
    distance[0] = 0

# run this n-1 times
    for _ in range(0, len(WList.keys())):
        # finding the min distance of vertices stored in distance dictionary. initially for the starting vertex this is 0
        min_distance = min([distance[v]
                           for v in WList.keys() if not visited[v]])

        min_vertex_list = [v for v in WList.keys() if (
            not visited[v] and distance[v] <= min_distance)]

        min_vertex = min(min_vertex_list)
        # once the vertex is finalized we are exploring so mark that vertex as visited[v]=True

        visited[min_vertex] = True
        for v, d in WList[min_vertex]:
            if not visited[v]:
                if d < distance[v]:
                    distance[v] = d
                    edge_in_MST[v] = min_vertex
    return edge_in_MST


if __name__ == "__main__":
    weighted_graph = {
        0: [(1, 2), (3, 6)],
        1: [(0, 2), (2, 3), (3, 8)],
        2: [(1, 3), (3, 4), (4, 5)],
        3: [(0, 6), (1, 8), (2, 4), (4, 7)],
        4: [(2, 5), (3, 7)]
    }

    print("Connected weighted graph:")
    print(weighted_graph)
    print("\nPrim's MST parent mapping:")
    print(prim_MST(weighted_graph))
