# max heap implementation

class MaxHeap:
    """Array-based max heap where every parent is at least its children."""

    def __init__(self):
        """Create an empty max heap."""
        self.A = []

    def build_maxHeap(self, L: list) -> None:
        """Build a max heap from the elements in ``L`` in O(n) time."""
        self.A = []
        for element in L:
            self.A.append(element)

        median = (len(self.A)//2)-1
        for i in range(median, -1, -1):
            self.max_heapify(i)

    def max_heapify(self, i):
        """Restore max-heap order below index ``i`` in O(log n) time."""
        left = i*2 + 1
        right = i*2 + 2
        maximum = i
        if left < len(self.A) and self.A[left] > self.A[maximum]:
            maximum = left
        if right < len(self.A) and self.A[right] > self.A[maximum]:
            maximum = right
        if maximum != i:
            self.A[maximum], self.A[i] = self.A[i], self.A[maximum]
            return self.max_heapify(maximum)

    def delete_max(self):
        """Remove and return the largest element, or ``None`` if empty."""
        result = None
        if self.A != []:
            self.A[0], self.A[-1] = self.A[-1], self.A[0]
            result = self.A.pop()
            self.max_heapify(0)
        return result

    def insert(self, element):
        """Add ``element`` and restore heap order in O(log n) time."""
        self.A.append(element)
        index = len(self.A)-1
        while index > 0:
            parent = (index-1)//2
            if self.A[index] > self.A[parent]:
                self.A[index], self.A[parent] = self.A[parent], self.A[index]
                index = parent
            else:
                break

    def __str__(self):
        return str(self.A)


heap = MaxHeap()
heap.build_maxHeap([4, 2, 56, 34, 788, 64, 1])
print(heap)
