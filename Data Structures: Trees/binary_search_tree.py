class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        return f'{{val: {self.val}, left: {self.left}, right: {self.right}}}'


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __str__(self):
        if self.root is None:
            return '{val: None, left: None, right: None}'
        return str(self.traverse(self.root))

    def traverse(self, node):
        tree = node
        tree.left = None if node.left is None else self.traverse(node.left)
        tree.right = None if node.right is None else self.traverse(node.right)
        return tree
    
    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            curr = self.root
            while curr:
                if val < curr.val:
                    if curr.left is None:
                        curr.left = Node(val)
                        break
                    curr = curr.left
                elif val > curr.val:
                    if curr.right is None:
                        curr.right = Node(val)
                        break
                    curr = curr.right
                else:
                    return False
        return True

    def lookup(self, val):
        if self.root is None:
            return False
        curr = self.root
        while curr:
            if val < curr.val:
                if curr.left is None:
                    return False
                curr = curr.left
            elif val > curr.val:
                if curr.right is None:
                    return False
                curr = curr.right
            else:
                return True

    def remove(self, val):
        if self.root is None:
            return False
        curr = self.root
        parent = None
        while curr:
            if val < curr.val:
                if curr.left is None:
                    return False
                parent = curr
                curr = curr.left
            elif val > curr.val:
                if curr.right is None:
                    return False
                parent = curr
                curr = curr.right
            else:
                # 1: target node is a leaf
                if curr.left is None and curr.right is None:
                    if parent is None:
                        self.root = None
                    elif parent.left == curr:
                        parent.left = None
                    else:
                        parent.right = None
                # 2: target node has a child
                elif curr.left and curr.right is None:
                    if parent is None:
                        self.root = curr.left
                    elif parent.left == curr:
                        parent.left = curr.left
                    else:
                        parent.right = curr.left
                elif curr.left is None and curr.right:
                    if parent is None:
                        self.root = curr.right
                    elif parent.left == curr:
                        parent.left = curr.right
                    else:
                        parent.right = curr.right
                # 3: target node has two children
                else:
                    s = curr.right      # successor
                    sp = None           # successor's parent
                    while s.left:
                        sp = s
                        s = s.left
                    
                    # print(str(sp))
                    # print(str(s))

                    if parent is None:
                        if sp is not None:
                            if s.right:
                                sp.left = s.right
                            else:
                                sp.left = None
                        s.left = self.root.left
                        s.right = self.root.right
                        self.root = s
                    else:
                        if sp is not None:
                            if s.right:
                                sp.left = s.right
                            else:
                                sp.left = None
                        s.left = curr.left
                        s.right = curr.right
                        if parent.left == curr:
                            parent.left = s
                        else:
                            parent.right = s
                return True
