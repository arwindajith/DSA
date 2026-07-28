class queue:
    def __init__(self):
        self.q = []

    def enqueue(self, value):
        self.q.append(value)

    def dequeue(self):
        if self.isempty():
            return None
        else:
            result = self.q[0]
            self.q = self.q[1:]
            return result

    def isempty(self):
        if len(self.q) == 0:
            return True
        return False


def BFS(Alist, start):
    visited = {}
    for value in Alist.keys():
        visited[value] = False

    q = queue()
    q.enqueue(start)
    visited[start] = True

    while not q.isempty():
        temp_vertex = q.dequeue()
        for vertex in Alist[temp_vertex]:
            if not visited[vertex]:
                visited[vertex] = True
                q.enqueue(vertex)
    return visited


def components_BFS(Alist):
    component = {}
    for vertex in Alist.keys():
        component[vertex] = -1
    comp_id, seen = 0, 0

    while seen <= max(Alist.keys()):
        start_vertex = min([i for i in Alist.keys() if component[i] == -1])

        visited = BFS(Alist, start_vertex)

        for vertex in visited.keys():
            if visited[vertex] is True:
                component[vertex] = comp_id
                seen += 1
        comp_id += 1

    return component


def random_adjacency(n, edge_prob=0.1, directed=False, allow_self_loops=False, seed=None, start_index=0):
    """
    Create an adjacency list for `n` vertices with random edges.
    - n: number of vertices
    - edge_prob: probability of adding each possible edge (0..1)
    - directed: if False, edges are undirected
    - allow_self_loops: whether to allow edges from a node to itself
    - seed: optional RNG seed for reproducibility
    - start_index: starting vertex id (0 or 1 typically)
    Returns: dict vertex -> list of neighbors
    """
    import random
    if seed is not None:
        random.seed(seed)
    nodes = list(range(start_index, start_index + n))
    adj = {v: [] for v in nodes}
    for u in nodes:
        for v in nodes:
            if not allow_self_loops and u == v:
                continue
            if not directed and v <= u:
                continue
            if random.random() < edge_prob:
                adj[u].append(v)
                if not directed:
                    adj[v].append(u)
    return adj


Alist1 = random_adjacency(9)
print(components_BFS(Alist1))
