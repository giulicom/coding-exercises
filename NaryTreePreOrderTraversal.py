"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        order = []
        if root != None:
            order.append(root.val)

            queue = root.children
            while len(queue) > 0:
                child = queue[0]
                queue.remove(child)
                order.append(child.val)
                queue = child.children + queue

        return order