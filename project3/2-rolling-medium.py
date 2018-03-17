from minheap import *
from maxheap import *
import sys

#collaborated with Austin Long

def driver():

    minHeap = MinHeap()
    maxHeap = MaxHeap()

    with open(sys.argv[1]) as f:

        n = int(f.readline().strip())

        minHeap.insert(int(f.readline().strip())) #insert first number to minheap
        print(minHeap.look()) #median is the single element

        for _ in range(n-1):

            in_data = int(f.readline().strip())

            if in_data >= minHeap.look(): #insert number into proper tree
                minHeap.insert(in_data)
            else:
                maxHeap.insert(in_data)
            
            if abs(minHeap.size() - maxHeap.size()) > 1: #balance trees 
                if minHeap.size() > maxHeap.size():
                    maxHeap.insert(minHeap.remove())
                else:
                    minHeap.insert(maxHeap.remove())
            
            if ((minHeap.size() + maxHeap.size()) % 2 == 0): #if total number of elements is even median is sum of middle numbers/2
                middle = (minHeap.look() + maxHeap.look())
                median = middle / 2
                if middle % 2 == 0: #if sum of roots is even
                    print(int(median))
                else: #if sum of roots is odd
                    print("{0:0.1f}".format(median))

            else: #if total number of elements is odd median is root of bigger tree
                if minHeap.size() > maxHeap.size():
                    print(minHeap.look())
                else:
                    print(maxHeap.look())

if __name__ == "__main__":
    driver()