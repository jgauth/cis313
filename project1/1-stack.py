from double_ll import DoubleLL
import sys
from copy import copy

class Stack(DoubleLL):
    """Stack data structure implemented using a doubly linked list"""
    def __init__(self):
        super().__init__()

    def is_empty(self):
        return (self.size == 0)

    def push(self, x):
        self.insert(x)

    def pop(self):
        if self.head == None:
            return("StackError")
        else:
            data = self.head.data
            self.delete_head()
            return data

def print_stack(s):
    if s.is_empty():
        print("Empty")
        return
    s_copy = copy(s)
    data_list = []
    while not(s_copy.is_empty()):
        data_list.append(s_copy.pop())
    out = " ".join(str(x) for x in data_list)
    print(out)


def driver():
    s = Stack()
    with open(sys.argv[1]) as f:
        n = int(f.readline().strip())
        for _ in range(n):
            in_data = f.readline().strip().split()
            action, value_option = in_data[0], in_data[1:]
            if action == "push":
                value = int(value_option[0])
                s.push(value)
            elif action == "pop":
                print(s.pop())
            elif action == "print":
                print_stack(s)

# this starter code should work with either python or python3
if __name__ == "__main__":
    driver()
