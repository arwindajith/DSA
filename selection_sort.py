def selection_sort(L):
    n = len(L)
    if n <= 1:
        return L
    for i in range(n):
        min_position = i
        for j in range(i+1, n, 1):
            if L[j] < L[min_position]:
                min_position = j
        L[i], L[min_position] = L[min_position], L[i]

    return L


print(selection_sort([2, 7, 4, 6, 27, 10, 53]))
