def insertion_sort(L):
    n = len(L)
    if n <= 1:
        return L
    for i in range(n):
        pointer = i
        while (pointer > 0 and L[pointer] < L[pointer-1]):
            L[pointer], L[pointer-1] = L[pointer-1], L[pointer]
            pointer -= 1

    return L


print(insertion_sort([2, 7, 4, 6, 27, 10, 53]))
