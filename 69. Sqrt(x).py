class Solution(object):
    def mySqrt(self, x):
        l, r = 0, x
        while l < r:
            mid = r + l + 1 >> 1
            if mid * mid <= x:
                l = mid
            else:
                r = mid - 1
        return r
