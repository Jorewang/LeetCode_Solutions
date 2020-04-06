class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        right = left = up = down = 0
        for m in moves:
            if m == 'R':
                right += 1
            if m == 'L':
                left += 1
            if m == 'U':
                up += 1
            if m == 'D':
                down += 1
        if right == left and up == down:
            return True
        else:
            return False
