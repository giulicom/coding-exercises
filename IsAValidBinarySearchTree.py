class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

def isValid(root, min, max):
    if root == None:
        return True
    if root.info <= min or root.info >= max:
        return False

    return isValid(root.left, min, root.info) and isValid(root.right, root.info, max)


if __name__ == '__main__':
    tree = BinarySearchTree()
    t = 5
    arr = [5, 7, 2, 3, 9]
    for i in range(t):
        tree.create(arr[i])

    res = isValid(tree.root, 0, 10**4)
    print(res)
