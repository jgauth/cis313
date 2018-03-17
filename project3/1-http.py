import sys
import pdb
from minheap import MinHeap

#collaborated with Austin Long

def driver():

    heapA = MinHeap()
    heapB = MinHeap()
    dictA = {}
    dictB = {}
    
    with open(sys.argv[1]) as f:
        n = int(f.readline().strip())
        for _ in range(n):

            in_data = f.readline().strip().split()
            ip, tier, time = in_data[0], in_data[1], int(in_data[2])

            if tier == "A":
                heapA.insert(time)
                if time not in dictA.keys():
                    dictA[time] = []
                dictA[time].append(ip)
            elif tier == "B":
                heapB.insert(time)
                if time not in dictB.keys():
                    dictB[time] = []
                dictB[time].append(ip)
    serve_requests(heapA, dictA)
    serve_requests(heapB, dictB)


def serve_requests(heap, dict):
    for _ in range(heap.size()):
        time = heap.remove()
        ip = dict[time].pop(0)
        print(ip)


if __name__ == "__main__":
    driver()
