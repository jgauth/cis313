# Author: John Gauthier
# Description: Doubly linked list  

class DoubleLL(object):
    class LLNode(object):
        def __init__(self, data=None):
            self.data = data
            self.next = None
            self.prev = None

    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None


    def insert(self, x):
        node = self.LLNode(x)
        node.next = self.head
        if self.head == None:
            self.tail = node
        else:
            self.head.prev = node
        self.head = node
        self.size += 1


    #Assumes that calling this on empty LL error will be handled elsewhere
    def delete_head(self):
        if self.head.next == None:
            self.head = None
            self.tail = None
        else:
            self.head.next.prev = None
            self.head = self.head.next
        self.size -= 1

    #Assumes that calling this on empty LL error will be handled elsewhere
    def delete_tail(self):
        if self.tail.prev == None:
            self.head = None
            self.tail = None
        else:
            self.tail.prev.next = None
            self.tail = self.tail.prev
        self.size -= 1
