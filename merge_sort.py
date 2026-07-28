"""def merge(Left, Right):
    n, m = len(Left), len(Right)
    C, i, j, k = [], 0, 0, 0

    while k < n+m:
        if i == n:
            C.extend(Right[j:])
            k = k+(n-j)
        elif j == m:
            C.extend(Left[i:])
            k = k+(n-i)
        elif Left[i] <= Right[j]:
            C.append(Left[i])
            i, k = i+1, k+1
        else:
            C.append(Right[j])
            j, k = j+1, k+1

    return C"""


def merge(A, B):
    len_A, len_B = len(A), len(B)
    c, i, j = [], 0, 0

    while i < len_A and j < len_B:
        if A[i] <= B[j]:
            c.append(A[i])
            i += 1
        else:
            c.append(B[j])
            j += 1
    while i < len_A:
        c.append(A[i])
        i += 1
    while j < len_B:
        c.append(B[j])
        j += 1
    return c


def merge_sort(L):
    n = len(L)
    if n <= 1:
        return L

    Left = merge_sort(L[:n//2])
    Right = merge_sort(L[n//2:])

    C = merge(Left, Right)
    return C


print(merge_sort([2, 7, 4, 6, 27, 10, 53]))
