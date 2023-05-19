class Node:
    def __init__(self, value):
        self.key = value
        self.left = None
        self.right = None
        self.parent = None

def rightRotate(node):
    if node is None or node.left is None:
        return node
    parent = node.parent
    left = node.left
    left_right = left.right

    # change edge 1
    if parent: # find out if node is a left or right child of node
        if parent.left == node:
            parent.left = left
        else:
            parent.right = left
    left.parent = parent

    # change edge 2
    left.right = node
    node.parent = left

    # change edge 3
    node.left = left_right
    if left_right:
        left_right.parent = node

    return left  # the node that took the position of node

# your code to build the tree
n_12 = Node(12)
n_15 = Node(15)
n_3 = Node(3)
n_7 = Node(7)
n_1 = Node(1)
n_2 = Node(2)
n_not1 = Node(-1)

n_12.right = n_15
n_12.left = n_3
n_3.right = n_7
n_3.left = n_1
n_1.right = n_2
n_1.left = n_not1

n_12.parent = None
n_15.parent = n_12
n_3.parent = n_12
n_7.parent = n_3
n_1.parent = n_3
n_2.parent = n_1
n_not1.parent = n_1

# rotate the root
root = n_12
root = rightRotate(root) # returns the node that took the place of n_12