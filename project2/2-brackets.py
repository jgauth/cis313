import sys

def check_brackets(s):
    stack = []
    open_brackets = '[{(<'

    for c in s:

        if c in open_brackets:
            stack.append(c)

        elif (len(stack) != 0):
            x = stack.pop()
            if not ((x == '[' and c == ']') or #compare current character to stack.pop()
                    (x == '{' and c == '}') or #if they don't 'match' prints No and returns
                    (x == '(' and c == ')') or
                    (x == '<' and c == '>')):
                    print("NO")
                    return
        else:
            print("NO")
            return
    print("YES")


def driver():

    with open(sys.argv[1]) as f:

        n = int(f.readline().strip())

        for _ in range(n):

            s = f.readline().strip()
            check_brackets(s)


if __name__ == "__main__":
    driver()
