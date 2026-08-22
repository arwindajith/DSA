class min_heap:
    def __init__(self):
        self.A = []

    def build_minHeap(self, L):
        self.A = []
        for element in L:
            self.A.append(element)
        median = (len(self.A)//2)-1
        for i in range(median, -1, -1):
            self.min_heapify(i)

    def min_heapify(self, i):
        left = 2*i + 1
        right = 2*i + 2
        minimum = i
        size_of_list = len(self.A)
        if left < size_of_list and self.A[left] < self.A[minimum]:
            minimum = left
        if right < size_of_list and self.A[right] < self.A[minimum]:
            minimum = right
        if minimum != i:
            self.A[minimum], self.A[i] = self.A[i], self.A[minimum]
            return self.min_heapify(minimum)

    def delete(self):
        result = None
        if self.A != []:
            self.A[0], self.A[-1] = self.A[-1], self.A[0]
            result = self.A.pop()
            self.min_heapify(0)

        return result

    def insert(self, element):
        self.A.append(element)
        index = len(self.A)-1

        while index > 0:
            parent = (index-1)//2
            if self.A[index] < self.A[parent]:
                self.A[index], self.A[parent] = self.A[parent], self.A[index]
                index = parent
            else:
                break
