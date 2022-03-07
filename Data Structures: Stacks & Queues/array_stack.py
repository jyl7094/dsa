class Node:
    def __init__(self, val):
        self.val = val


class Stack:
    def __init__(self):
        self.ary = []

    def peek(self):
        if not self.ary:
            return
        return self.ary[-1].val
    
    def push(self, val):
        self.ary.append(Node(val))

    def pop(self):
        return self.ary.pop().val
    
    def isEmpty(self):
        return not self.ary
