visited, pre, post = {}, {}, {}


def initPrePost(AList):
    for vertex in AList.keys():
        visited[vertex] = False
        pre[vertex], post[vertex] = -1, -1
    return


def assignPrePostDFS(Alist, vertex, count):
    visited[vertex] = True
    pre[vertex] = count
    count += 1

    for v in Alist[vertex]:
        if not visited[v]:
            count = assignPrePostDFS(Alist, v, count)
    post[vertex] = count
    count += 1
    return count
