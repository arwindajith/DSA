# quick sort is usually the go to algorithm if it is inplace.
def partition(L, lower, upper):
    pivot = L[lower]
    i = lower
    for j in range(lower+1, upper+1):
        if L[j] < pivot:
            i = i+1
            L[i], L[j] = L[j], L[i]
    L[lower], L[i] = L[i], L[lower]
    return i


def quick_sort(L, lower, upper):
    if lower < upper:
        pivot_position = partition(L, lower, upper)
        quick_sort(L, lower, pivot_position)
        quick_sort(L, pivot_position+1, upper)
    return L


l1 = [1, 5, 3, 8, 9, 4, 2]
quick_sort(l1, 0, len(l1)-1)
