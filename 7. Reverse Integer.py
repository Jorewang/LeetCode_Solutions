class Solution(object):
    def reverse(self, x):

        s = str(abs(x))[::-1]
        if x < 0:
            ans = -int(s)
        else:
            ans = int(s)

        return ans if -(1 << 31) <= ans <= (1 << 31)-1 else 0


if __name__ == '__main__':
    print(Solution().reverse(-1563847412))
