class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def longestUnivaluePath(self, root):
        return self.helper(root)[2]

    def helper(self, root):
        val = root.val
        has_root = False
        length = 0
        if root is None:
            return (True, 0, length)
        l_has_root, l_val, l_length = self.helper(root.left)
        r_has_root, r_val, r_length = self.helper(root.right)
        if l_val == r_val == root.val:
            val = root.val
            length = l_length + r_length + 2
            has_root = True
        elif l_val == root.val:
            if l_length+1 >= r_length:
                has_root = True
                length = l_length + 1
                val = root.val
            else:
                has_root = False
                length = r_length
                val = r_val
        elif r_val == root.val:
            if r_length+1 >= l_length:
                has_root = True
                length = r_length + 1
                val = root.val
            else:
                has_root = False
                length = l_length
                val = l_val
        else:
            has_root = False
            length = max(r_length, l_length)
            val = r_val if r_length >= l_length else l_val

        return (has_root, val, length)
