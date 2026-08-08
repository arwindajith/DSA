def floyd_warshall(Amat):
    n = len(Amat)
    SP = [[float('inf') for _ in range(n)] for _ in range(n)]

    for row in range(n):
        for col in range(n):
            if row == col:
                SP[row][col] = 0
            elif Amat[row][col][0] == 1:
                SP[row][col] = Amat[row][col][1]
            else:
                SP[row][col] = float('inf')

    for k in range(n):
        for i in range(n):
            for j in range(n):
                SP[i][j] = min(SP[i][j], SP[i][k] + SP[k][j])
    return SP


# Example adjacency matrix for a directed graph with both positive and negative edge weights.
# Each entry is (has_edge, weight). A value of (0, 0) means no edge.
# This layout is a DAG, so it has negative edges but no negative cycle.
Amat = [
    [(1, 0), (1, 4), (1, -2), (0, 0), (0, 0), (0, 0), (0, 0)],
    [(0, 0), (1, 0), (1, 3), (1, -1), (0, 0), (0, 0), (0, 0)],
    [(0, 0), (0, 0), (1, 0), (1, 2), (1, -3), (0, 0), (0, 0)],
    [(0, 0), (0, 0), (0, 0), (1, 0), (1, 5), (1, -4), (0, 0)],
    [(0, 0), (0, 0), (0, 0), (0, 0), (1, 0), (1, 1), (1, -2)],
    [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (1, 0), (1, 6)],
    [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (1, 0)]
]

# Test the function
result = floyd_warshall(Amat)
print("All-pairs shortest paths:")
for row in result:
    print(row)
