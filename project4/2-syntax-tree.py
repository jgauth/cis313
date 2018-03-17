import sys

class STNode:

    def __init__(self, x: str):
        self.key = x
        self.left = None
        self.right = None
        self.p = None


class SyntaxTree:

    def init_helper(self, i: int, l: 'list of strings') -> STNode:
        if i >= len(l):
            return None

        node = STNode(l[i])
        node.left = self.init_helper(2 * i + 1, l)
        node.right = self.init_helper(2 * i + 2, l)
        return node

    def __init__(self, l: 'list of strings') -> 'complete syntax tree':
        self.root = self.init_helper(0, l)

    def gen_expression(self, x):
        if x == None:
            return ''
        else:
            l = self.gen_expression(x.left)
            r = self.gen_expression(x.right)
            if x.key == '*' or x.key == '+' or x.key == '-':
                return '(' + l + x.key + r + ')'
            else:
                return l + x.key + r
    
    def evaluate(self, x):
        if x == None:
            return 0
        else:
            l = self.evaluate(x.left)
            r = self.evaluate(x.right)
            if x.key == '*':
                return l * r
            elif x.key == '+':
                return l + r
            elif x.key == '-':
                return l - r
            else:
                return int(x.key)        


def driver():

    with open(sys.argv[1]) as f:
        n = int(f.readline().strip())
        l = f.readline().strip().split()
        t = SyntaxTree(l)

        m = t.gen_expression(t.root)
        print(m)
        n = t.evaluate(t.root)
        print(n)


if __name__ == "__main__":
    driver()
