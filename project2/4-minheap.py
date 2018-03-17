# Author: John Gauthier
# Description: Minheap data structure

# Collaborated with Austin Long

import sys

class MinHeap(object):

    def __init__(self):
        self._size = 0 # keep track of size because array starts at 1,so len(array) returns size + 1
        self._array = [None] # heap starts at _array[1] so that I can use parent/child calculations

    def parent(self, i):
        return i//2

    def lchild(self, i):
        return 2*i

    def rchild(self, i):
        return 2*i + 1

    def bubble_up(self, i): #checks if parent element is greater than element. if yes, swaps their position and calls bubble_up again
        p = self.parent(i)
        if p >= 1:
            if self._array[p] > self._array[i]:
                temp = self._array[p]
                self._array[p] = self._array[i]
                self._array[i] = temp
                self.bubble_up(p)

    def bubble_down(self, i): #min-heapify
        l = self.rchild(i)
        r = self.lchild(i)
        if (l <= self._size and self._array[l] < self._array[i]):
            smallest = l
        else:
            smallest = i
        if (r <= self._size and self._array[r] < self._array[smallest]):
            smallest = r
        if smallest != i:
            temp = self._array[i]
            self._array[i] = self._array[smallest]
            self._array[smallest] = temp
            self.bubble_down(smallest)


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


def driver():
    m = MinHeap()
    with open(sys.argv[1]) as f:
        n = int(f.readline().strip())
        for _ in range(n):

            in_data = f.readline().strip().split()
            action, value_option = in_data[0], in_data[1:]

            if action == "insert":
                value = int(value_option[0])
                m.insert(value)

            elif action == "remove":
                print(m.remove())

            elif action == "print":
                print(m.to_string())

            elif action == "size":
                print(m.size())

            elif action == "best":
                print(m.look())

if __name__ == "__main__":
    driver()
