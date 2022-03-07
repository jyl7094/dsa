class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0
    
    def peek(self):
        if self.first is None:
            return
        return self.first.val

    def enqueue(self, val):
        if self.first is None:
            self.first = self.last = Node(val)
        else:
            self.last.next = self.last = Node(val)
        self.length += 1
    
    def dequeue(self):
        if self.first is None:
            return
        val = self.first.val
        self.first = self.first.next
        self.length -= 1
        return val
    
    def isEmpty(self):
        return not self.length
