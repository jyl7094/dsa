class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    
    def __str__(self):
        return str(self.val)

    
class LinkedList:
    def __init__(self):
        self.head = self.tail = None
        self.length = 0
    
    def __str__(self):
        curr = self.head
        nodes = []
        while curr:
            if curr.next is None:
                nodes.append(str(curr))
            else:
                nodes.append(f'{curr} -> ')
            curr = curr.next
        return (
            f'Linked List: {"".join(nodes)}\n'
            f'Head: {self.head if self.head else "None"}, '
            f'Tail: {self.tail if self.tail else "None"}, '
            f'Length: {self.length if self.length else "0"}'
        )
    
    def append(self, val):
        if self.head is None:
            self.head = self.tail = Node(val)
        else:
            self.tail.next = self.tail = Node(val)
        self.length += 1
    
    def prepend(self, val):
        if self.head is None:
            self.append(val)
        else:
            self.head = Node(val, self.head)
            self.length += 1
    
    def insert(self, index, val):
        if index > self.length or index < 0:
            raise IndexError
        if index == 0:
            self.prepend(val)
        elif index == self.length:
            self.append(val)
        else:
            curr = self.head
            for _ in range(index-1):
                curr = curr.next
            curr.next = Node(val, curr.next)
            self.length += 1
    
    def remove(self, index):
        if index >= self.length or index < 0:
            raise IndexError
        if index == 0:
            self.head = self.head.next
        else:
            curr = self.head
            for _ in range(index-1):
                curr = curr.next
            if curr.next == self.tail:
                curr.next = None
                self.tail = curr
            else:
                curr.next = curr.next.next
        self.length -= 1

    def reverse(self):
        if self.head is None:
            return
        nodes = []
        curr = self.head
        self.head, self.tail = self.tail, self.head
        while curr:
            nodes.insert(0, curr)
            curr = curr.next
        curr = self.head
        for i in range(len(nodes)-1):
            nodes[i].next = nodes[i+1]
        self.tail.next = None
