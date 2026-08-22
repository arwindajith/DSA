def max_heapify(A, size, i):
    left_child = i*2 + 1
    right_child = i*2 + 2
    maximum = i

    if left_child < size and A[left_child] > A[maximum]:
        maximum = left_child
    if right_child < size and A[right_child] > A[maximum]:
        maximum = right_child
    if i != maximum:
        A[i], A[maximum] = A[maximum], A[i]
        max_heapify(A, size, maximum)


def build_max(A):
    n = (len(A)//2)-1
    for i in range(n, -1, -1):
        max_heapify(A, len(A), i)


def heap_sort(A):
    n = len(A)
    build_max(A)
    for i in range(n-1, -1, -1):
        A[0], A[i] = A[i], A[0]
        max_heapify(A, i, 0)
