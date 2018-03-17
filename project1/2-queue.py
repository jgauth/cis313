# Author: John Gauthier
# Description: Queue data structure implemented with doubly linked list

from double_ll import DoubleLL
import sys
from copy import copy

class Queue(DoubleLL):
	"""Queue data structure implemented using a doubly linked list"""
	def __init__(self):
		super().__init__()

	def is_empty(self):
		return (self.size == 0)

	def enqueue(self, x):
		self.insert(x)

	def dequeue(self):
		if self.head == None:
			return("QueueError")
		else:
			data = self.tail.data
			self.delete_tail()
			return data

def print_queue(q):
    if q.is_empty():
        print("Empty")
        return
    q_copy = copy(q)
    data_list = []
    while not(q_copy.is_empty()):
        data_list.append(q_copy.dequeue())
    out = " ".join(str(x) for x in data_list)
    print(out)


def driver():
    q = Queue()
    with open(sys.argv[1]) as f:
        n = int(f.readline().strip())
        for _ in range(n):
            in_data = f.readline().strip().split()
            action, value_option = in_data[0], in_data[1:]
            if action == "enqueue":
                value = int(value_option[0])
                q.enqueue(value)
            elif action == "dequeue":
                print(q.dequeue())
            elif action == "print":
                print_queue(q)

# this starter code should work with either python or python3
if __name__ == "__main__":
    driver()
