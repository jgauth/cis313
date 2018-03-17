import sys

class MaxHeap(object):
    #source: adjusted code from my minheap.py from project 2

    def __init__(self):
        self._size = 0 # keep track of size because array starts at 1,so len(array) returns size + 1
        self._array = [None] # heap starts at _array[1] so that I can use parent/child calculations

    def parent(self, i):
        return i//2

    def lchild(self, i):
        return 2*i

    def rchild(self, i):
        return 2*i + 1

    def bubble_up(self, i): #checks if parent element is less than element. if yes, swaps their position and calls bubble_up again
        p = self.parent(i)
        if p >= 1:
            if self._array[p] < self._array[i]:
                temp = self._array[p]
                self._array[p] = self._array[i]
                self._array[i] = temp
                self.bubble_up(p)

    def bubble_down(self, i): #max-heapify
        l = self.rchild(i)
        r = self.lchild(i)
        if (l <= self._size and self._array[l] > self._array[i]):
            largest = l
        else:
            largest = i
        if (r <= self._size and self._array[r] > self._array[largest]):
            largest = r
        if largest != i:
            temp = self._array[i]
            self._array[i] = self._array[largest]
            self._array[largest] = temp
            self.bubble_down(largest)


    def insert(self, x):
        self._array.append(x)
        self._size += 1
        self.bubble_up(self._size)

    def remove(self):
        if self._size == 0:
            return "HeapError"
        elif self._size == 1:
            self._size -= 1
            return self._array.pop()
        else:
            value = self._array[1]
            self._array[1] = self._array.pop()
            self._size -= 1
            self.bubble_down(1)
            return value

    def look(self):
        if self._size == 0:
            return "HeapError"
        return self._array[1]

    def size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def to_string(self):
        if self._size == 0:
            return "Empty"

        return " ".join(str(x) for x in self._array[1:])