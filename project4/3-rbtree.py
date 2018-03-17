# Author: John Gauthier
# Description: Red-black tree data structure

import sys

class RBTree(object):
    
    class RBTreeNode(object):

        def __init__(self, key=None, color='RED'):
            self.key = key
            self.p = None
            self.left = None
            self.right = None
            self.color = color

    
    def __init__(self):
        self.nil = self.RBTreeNode(None, 'BLACK')
        self.root = self.nil

    def create_node(self, k):
        node = self.RBTreeNode(k)
        self.insert(node)
    
    
    def left_rotate(self, x): #assumes that x.right != T.nil and the root's p is T.nil
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.p = x
        y.p = x.p
        if x.p == self.nil:
            self.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.left = x
        x.p = y
    
    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.nil:
            y.right.p = x
        y.p = x.p
        if x.p == self.nil:
            self.root = y
        elif x == x.p.right:
            x.p.right = y
        else:
            x.p.left = y
        y.right = x
        x.p = y

    def insert(self, z):
        y = self.nil
        x = self.root
        while x != self.nil:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.p = y
        if y == self.nil:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        z.left = self.nil
        z.right = self.nil
        z.color = 'RED'
        self.insert_fixup(z)

    def insert_fixup(self, z):
        while z.p.color == 'RED':
            if z.p == z.p.p.left:
                y = z.p.p.right
                if y.color == 'RED':
                    z.p.color = 'BLACK'
                    y.color = 'BLACK'
                    z.p.p.color = 'RED'
                    z = z.p.p
                else:
                    if z == z.p.right:
                        z = z.p
                        self.left_rotate(z)
                    z.p.color = 'BLACK'
                    z.p.p.color = 'RED'
                    self.right_rotate(z.p.p)
            else:
                y = z.p.p.left
                if y.color == 'RED':
                    z.p.color = 'BLACK'
                    y.color = 'BLACK'
                    z.p.p.color = 'RED'
                    z = z.p.p
                else:
                    if z == z.p.left:
                        z = z.p
                        self.right_rotate(z)
                    z.p.color = 'BLACK'
                    z.p.p.color = 'RED'
                    self.left_rotate(z.p.p)
        self.root.color = 'BLACK'
    
    def transplant(self, u, v):
        if u.p == self.nil:
            self.root = v
        elif u == u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        v.p = u.p

    def minimum(self, x): #return node in the subtree rooted at x with the smallest key
        while x.left != self.nil:
            x = x.left
        return x

    def maximum(self, x):
        while x.right != self.nil:
            x = x.right
        return x

    def search(self, x, k):
        while (x != self.nil) and (x.key != k):
            if k < x.key:
                x = x.left
            else:
                x = x.right
        return x

    def delete(self, z):
        y = z
        y_color = y.color
        if z.left == self.nil:
            x = z.right
            self.transplant(z, z.right)
        elif z.right == self.nil:
            x = z.left
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_color = y.color
            x = y.right
            if y.p == z:
                x.p = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.p = y
            self.transplant(z, y)
            y.left = z.left
            y.left.p = y
            y.color = z.color
        if y_color == 'BLACK':
            self.delete_fixup(x)
    
    def delete_fixup(self, x):
        while x != self.root and x.color == 'BLACK':
            if x == x.p.left:
                w = x.p.right
                if w.color == 'RED':
                    w.color = 'BLACK'
                    x.p.color = 'RED'
                    self.left_rotate(x.p)
                    w = x.p.right
                if w.left.color == 'BLACK' and w.right.color == 'BLACK':
                    w.color = 'RED'
                    x = x.p
                else:
                    if w.right.color == 'BLACK':
                        w.left.color = 'BLACK'
                        w.color = 'RED'
                        self.right_rotate(w)
                        w = x.p.right
                    w.color  = x.p.color
                    x.p.color = 'BLACK'
                    w.right.color = 'BLACK'
                    self.left_rotate(x.p)
                    x = self.root
            else:
                w = x.p.left
                if w.color == 'RED':
                    w.color = 'BLACK'
                    x.p.color = 'RED'
                    self.right_rotate(x.p)
                    w = x.p.left
                if w.right.color == 'BLACK' and w.left.color == 'BLACK':
                    w.color = 'RED'
                    x = x.p
                else:
                    if w.left.color == 'BLACK':
                        w.right.color = 'BLACK'
                        w.color = 'RED'
                        self.left_rotate(w)
                        w = x.p.left
                    w.color  = x.p.color
                    x.p.color = 'BLACK'
                    w.left.color = 'BLACK'
                    self.right_rotate(x.p)
                    x = self.root
        x.color = 'BLACK'

    def to_list_inorder(self):
        l = []
        def inorder_walk(x):
            if x != self.nil:
                inorder_walk(x.left)
                l.append(x.key)
                inorder_walk(x.right)
        inorder_walk(self.root)
        return l

def driver():
    rbt = RBTree()

    with open(sys.argv[1]) as f:
        n = int(f.readline().strip())
        for _ in range(n):
            in_data = f.readline().strip().split()
            action, value_option = in_data[0], in_data[1:]

            if action == "insert":
                value = int(value_option[0])
                rbt.create_node(value)

            elif action == "remove":
                value = int(value_option[0])
                node = rbt.search(rbt.root, value)
                if node == rbt.nil:
                    print("TreeError")
                else:
                    rbt.delete(node)
            
            elif action == "search":
                value = int(value_option[0])
                node = rbt.search(rbt.root, value)
                if node == rbt.nil:
                    print("NotFound")
                else:
                    print("Found")

            elif action == "max":
                if rbt.root == rbt.nil:
                    print("Empty")
                else:
                    print(rbt.maximum(rbt.root).key)
            
            elif action == "min":
                if rbt.root == rbt.nil:
                    print("Empty")
                else:
                    print(rbt.minimum(rbt.root).key)
            
            elif action == "inprint":
                if rbt.root == rbt.nil:
                    print("Empty")
                else:
                    l = rbt.to_list_inorder()
                    print(" ".join(str(x) for x in l))

if __name__ == "__main__":
    driver()
