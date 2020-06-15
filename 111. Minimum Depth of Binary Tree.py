class Solution(object):
    def minDepth(self, root):
        if not root:
            return 0

        left = self.minDepth(root.left)
        right = self.minDepth(root.right)

        if not left or not right:
            return left + right + 1
        return min(left, right) + 1
    