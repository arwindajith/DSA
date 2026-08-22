"""An AVL tree is a self-balancing binary search tree.

It is also called Balanced search Tree

After every insertion or deletion, it keeps the height difference between a
node's left and right subtrees at most 1. Rotations restore balance when
needed, keeping search, insertion, and deletion operations efficient with
O(log n) time complexity.

Example: insert 30, then 20, then 10.

Before rebalancing, the tree leans too far to the left:

             30
            /
           20
          /
         10

The AVL tree performs a right rotation around 30:

             20
            /  \
           10   30

Now the tree is balanced. The values are still in search-tree order: smaller
values are on the left and larger values are on the right. In code, the
rotation is performed with `tree.right_rotate()`.
"""


class AVLTree:
    def __init__(self, value=None):
        self.value = value
        if self.value is not None:
            self.left = AVLTree()
            self.right = AVLTree()
            self.height = 1
        else:
            self.left = None
            self.right = None
            self.height = 0

    def isleaf(self):
        return (self.value is not None and self.left.value is None and self.right.value is None)

    def isempty(self):
        return (self.value is None and self.left is None and self.right is None)

    def inorder(self):
        if self.value is None:
            return []
        else:
            return self.left.inorder() + [self.value] + self.right.inorder()

    def preorder(self):
        if self.value is None:
            return []
        else:
            return [self.value] + self.left.preorder() + self.right.preorder()

    def postorder(self):
        if self.value is None:
            return []
        else:
            return self.left.postorder() + self.right.postorder() + [self.value]

    def left_rotate(self):
        # Save the current node and its three subtrees before rearranging them.
        v = self.value
        vr = self.right.value
        tl = self.left
        trl = self.right.left
        trr = self.right.right

        # The old root becomes the left child of its old right child.
        newleft = AVLTree(v)
        newleft.left = tl
        newleft.right = trl

        # The old right child moves up and becomes this subtree's new root.
        self.value = vr
        self.right = trr
        self.left = newleft

        return

    def right_rotate(self):
        # Save the current node and its three subtrees before rearranging them.
        v = self.value
        vl = self.left.value
        tr = self.right
        tll = self.left.left
        tlr = self.left.right

        # The old root becomes the right child of its old left child.
        newright = AVLTree(v)
        newright.left = tlr
        newright.right = tr

        # The old left child moves up and becomes this subtree's new root.
        self.value = vl
        self.left = tll
        self.right = newright

    def update_height(self):
        if self.isempty():
            return
        else:
            # Update children first, then calculate this node's height.
            self.left.update_height()
            self.right.update_height()
            self.height = 1 + max(self.left.height, self.right.height)

    def rebalance(self):
        # Measure the heights of the left and right sides.
        if self.left is None:
            hl = 0
        else:
            hl = self.left.height

        if self.right is None:
            hr = 0
        else:
            hr = self.right.height

        # If the left side is much taller, use a right rotation.
        if hl-hr > 1:
            if self.left.left.height > self.left.right.height:
                # Left-left case: one right rotation is enough.
                self.right_rotate()
            if self.left.left.height < self.left.right.height:
                # Left-right case: rotate the child left, then this node right.
                self.left.left_rotate()
                self.right_rotate()

            self.update_height()

        # If the right side is much taller, use a left rotation.
        if hl-hr < -1:
            if self.right.right.height > self.right.left.height:
                # Right-right case: one left rotation is enough.
                self.left_rotate()
            if self.right.right.height < self.right.left.height:
                # Right-left case: rotate the child right, then this node left.
                self.right.right_rotate()
                self.left_rotate()
            self.update_height()

    def insert(self, v):
        if self.isempty():
            self.value = v
            self.left = AVLTree()
            self.right = AVLTree()
            self.height = 1
            return
        if self.value == v:
            return
        if v < self.value:
            self.left.insert(v)
            self.rebalance()
            self.height = 1+max(self.left.height, self.right.height)

        if v > self.value:
            self.right.insert(v)
            self.rebalance()
            self.height = 1+max(self.left.height, self.right.height)
