class union_find:
    def __init__(self):
        self.component = {}
        self.members = {}
        self.size = {}

    def make_union_find(self, vertices):
        if vertices:
            for k in vertices:
                self.component[k] = k
                self.members[k] = [k]
                self.size[k] = 1

    def find(self, v):
        return self.component[v]

    def union(self, u, v):
        left = self.component[u]
        right = self.component[v]
        if left != right:
            if self.size[left] >= self.size[right]:
                for x in self.members[right]:
                    self.component[x] = left
                    self.members[left].append(x)
                    self.size[left] += 1
                del self.members[right]
                del self.size[right]
            else:
                for x in self.members[left]:
                    self.component[x] = right
                    self.members[right].append(x)
                    self.size[right] += 1
                del self.members[left]
                del self.size[left]
