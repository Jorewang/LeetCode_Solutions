class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        if not root.children:
            return 1
        tmp = 0
        for child in root.children:
            tmp = max(tmp, self.maxDepth(child) + 1)

        return tmp