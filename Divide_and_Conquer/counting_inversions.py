def merge_and_count(A, B):
    m, n = len(A), len(B)
    c, i, j, k = ([], 0, 0, 0)
    count = 0
    while k < m+n:
        if i == m:
            c.append(B[j])
            j, k = j+1, k+1
        elif j == n:
            c.append(A[i])
            i, k = i+1, k+1
        elif A[i] < B[j]:
            c.append(A[i])
            i, k = i+1, k+1
        else:
            c.append(B[j])
            j, k, count = j+1, k+1, m-i
    return (count, c)


def sort_and_count(A):
    if len(A) == 1:
        return (0, A)

    count_left, left = sort_and_count(A[:len(A)//2])
    count_right, right = sort_and_count(A[len(A)//2:])
    count_b, B = merge_and_count(left, right)

    return B, count_b+count_left+count_right
