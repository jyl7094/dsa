class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f'{{ val: {self.val}, left: {self.left}, right: {self.right} }}'


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            curr = self.root
            while True:
                if val > curr.val:
                    if curr.right is None:
                        curr.right = Node(val)
                        return True
                    curr = curr.right
                elif val < curr.val:
                    if curr.left is None:
                        curr.left = Node(val)
                        return True
                    curr = curr.left
                else:
                    return False

    def lookup(self, val):
        if self.root is None:
            return False
        curr = self.root
        while True:
            if val > curr.val:
                if curr.right is None:
                    return False
                curr = curr.right
            elif val < curr.val:
                if curr.left is None:
                    return False
                curr = curr.left
            else:
                return curr

    def remove(self, val):
        """
        Does not support removing the root
        """
        if self.root is None:
            return False
        curr = self.root
        parent = None
        while True:
            if val > curr.val:
                if curr.right is None:
                    return False
                parent = curr
                curr = curr.right
            elif val < curr.val:
                if curr.left is None:
                    return False
                parent = curr
                curr = curr.left
            else:
                # case 1: no child
                if curr.left is None and curr.right is None:
                    if parent.left == curr:
                        parent.left = None
                    else:
                        parent.right = None
                # case 2: one child
                elif curr.left is None and curr.right is not None:
                    if parent.left == curr:
                        parent.left = curr.right
                    else:
                        parent.right = curr.right
                elif curr.left is not None and curr.right is None:
                    if parent.left == curr:
                        parent.left = curr.left
                    else:
                        parent.right = curr.left
                # case 3: two children
                else:
                    #find min from the right subtree
                    min_node = curr.right
                    while min_node.left:
                        min_node_parent = min_node
                        min_node = min_node.left
                    # replace curr <-> min
                    if parent.left == curr:
                        parent.left = min_node
                    else:
                        parent.right = min_node
                    min_node_parent.left = min_node.right if min_node.right is not None else None
                    min_node.left = curr.left
                    min_node.right = curr.right
                    #delete last one
                return True


def traverse(node):
    """
    Print this function to see the BST object
    """
    tree = Node(node.val)
    tree.left = None if node.left is None else traverse(node.left)
    tree.right = None if node.right is None else traverse(node.right)
    return tree 
