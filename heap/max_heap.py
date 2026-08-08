class maxheap:
    def __init__(self):
        self.A = []

    def max_heapify(self, v):
        left_child = (2*v) + 1
        right_child = (2*v) + 2
        maximum = v

        if left_child < len(self.A) and self.A[left_child] > self.A[maximum]:
            maximum = left_child
        if right_child < len(self.A) and self.A[right_child] > self.A[maximum]:
            maximum = right_child
        if maximum != v:
            self.A[v], self.A[maximum] = self.A[maximum], self.A[v]
            self.max_heapify(maximum)

    def build_max_heap(self, L):
        self.A = []
        for vertex in L:
            self.A.append(vertex)

        n = int((len(self.A)//2)-1)
        for k in range(n-1, -1, -1):
            self.max_heapify(k)

    def del_max(self):
        vertex = None
        if len(self.A):
            self.A[0], self.A[len(self.A)-1] = self.A[len(self.A)-1], self.A[0]
            vertex = self.A.pop()
            self.max_heapify(0)
        return vertex
# in case of insert v stands for the actual vertex and not the index of the vertex

    def insert(self, v):
        self.A.append(v)
        index = len(self.A)-1
        while index > 0:
            parent = (index-1)//2
            if self.A[parent] < self.A[index]:
                self.A[parent], self.A[index] = self.A[index], self.A[parent]
                index = parent
            else:
                break
