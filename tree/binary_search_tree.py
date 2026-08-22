class Tree:
    def __init__(self, value=None):
        self.value = value
        if self.value is not None:
            self.left = Tree()
            self.right = Tree()
        else:
            self.left = None
            self.right = None

    def isleaf(self):
        if self.value is not None:
            if self.left.value is None and self.right.value is None:
                return True

        return False

    def isempty(self):
        return (not self.value and not self.left and not self.right)

    def in_order(self):
        if self.value is None:
            return []
        else:
            return self.left.in_order() + [self.value] + self.right.in_order()

    def find(self, v):
        """ find value v in tree """
        if self.isempty():
            return False
        if self.value == v:
            return True
        if v > self.value:
            self.right.find(v)
        if v < self.value:
            self.left.find(v)

    def minval(self):
        if self.left.isempty():
            return self.value
        else:
            self.left.minval()

    def maxval(self):
        if self.right.isempty():
            return self.value
        else:
            self.right.maxval()

    def insert(self, v):
        """inserting value v into the tree"""
        if self.isempty():
            self.value = v
            self.left = Tree()
            self.right = Tree()
        if self.value == v:
            return
        if v > self.value:
            self.right.insert(v)
            return
        if v < self.value:
            self.left.insert(v)
            return

    def makeempty(self):
        """converting leaf node to empty node"""
        self.value = None
        self.left = None
        self.right = None
        return

    def copyleft(self):
        self.value = self.left.value
        self.right = self.left.right
        self.left = self.left.left
        return

    def copyright(self):
        self.value = self.right.value
        self.left = self.right.left
        self.right = self.right.right
        return

    def delete(self, v):
        """ delete and element from tree"""
        if self.isempty():
            return
        if v < self.value:
            self.left.delete(v)
            return
        if v > self.value:
            self.right.delete(v)
            return
        if v == self.value:
            if self.isleaf():
                self.makeempty()
            elif self.left.isempty():
                self.copyright()
            elif self.right.isempty():
                self.copyleft()
            else:
                self.value = self.left.maxval()
                self.left.delete(self.left.maxval())
            return
