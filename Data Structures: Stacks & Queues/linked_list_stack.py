class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0
    
    def peek(self):
        if self.top is None:
            return
        return self.top.val
    
    def push(self, val):
        if self.isEmpty():
            self.top = self.bottom = Node(val)
        else:
            self.top.next = self.top = Node(val)
        self.length += 1
    
    def pop(self):
        if self.isEmpty():
            return
        elif self.length == 1:
            val = self.top.val
            self.top = self.bottom = None
        else:
            curr = self.bottom
            while curr.next != self.top:
                curr = curr.next
            val = curr.next.val
            self.top = curr
            self.top.next = None
        self.length -= 1
        return val

    def isEmpty(self):
        return not self.length
