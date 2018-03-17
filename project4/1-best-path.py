import sys

class BST(object):
    
    class BSTNode(object):

        def __init__(self, key=None):
            self.key = key
            self.parent = None
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def create_node(self, k): #create node with key k, then insert to tree
        node = self.BSTNode(k)
        self.insert(node)

    def insert(self, z): #insert node x (x != key)
        y = None
        x = self.root

        while x != None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right

        z.parent = y
        if y == None: #Tree was empty, so set root = z
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def search(self, x, k):
        while (x != None) and (x.key != k):
            if k < x.key:
                x = x.left
            else:
                x = x.right
        return x
    
    def minimum(self, x): #return node in the subtree rooted at x with the smallest key
        while x.left != None:
            x = x.left
        return x
    
    def maximum(self, x): #return node in the subtree rooted at x with the largest key
        while x.right != None:
            x = x.right
        return x
    
    def successor(self, x): #return successor of node x if it exists, and None if x has the largest key
        if x.right != None:
            return self.minimum(x.right)
        y = x.parent

        while (y != None) and (x == y.right):
            x = y
            y = y.parent
        return y

    def transplant(self, u, v): #replaces subtree rooted at node u with the subtree rooted at node v
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v != None:
            v.parent = u.parent

    def remove(self, z): #remove node z from the tree
        if z.left == None:
            self.transplant(z, z.right)
        elif z.right == None:
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            if y.parent != z:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y

    def to_list_inorder(self):
        l = []
        def inorder_walk(x):
            if x != None:
                inorder_walk(x.left)
                l.append(x.key)
                inorder_walk(x.right)
        inorder_walk(self.root)
        return l

    def to_list_preorder(self):
        l = []
        def preorder_walk(x):
            if x != None:
                l.append(x.key)
                preorder_walk(x.left)
                preorder_walk(x.right)
        preorder_walk(self.root)
        return l

    def to_list_postorder(self):
        l = []
        def postorder_walk(x):
            if x != None:
                postorder_walk(x.left)
                postorder_walk(x.right)
                l.append(x.key)
        postorder_walk(self.root)
        return l

    def best_path(self, x):
        if x == None:
            return 0
        else:
            l = self.best_path(x.left)
            r = self.best_path(x.right)
            return max(l,r) + str(x.key).count('5')


def driver():
    bst = BST()

    with open(sys.argv[1]) as f:
        n = int(f.readline().strip())
        for _ in range(n):
            in_data = f.readline().strip().split()
            action, value_option = in_data[0], in_data[1:]

            if action == "insert":
                value = int(value_option[0])
                bst.create_node(value)

            elif action == "remove":
                value = int(value_option[0])
                node = bst.search(bst.root, value)
                if node == None:
                    print("TreeError")
                else:
                    bst.remove(node)
            
            elif action == "bpv":
                if bst.root == None:
                    print("TreeError")
                else:
                    l = bst.best_path(bst.root)
                    print(l)

if __name__ == "__main__":
    driver()