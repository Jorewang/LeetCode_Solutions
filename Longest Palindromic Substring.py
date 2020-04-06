class Solution(object):
    def longstPalindrome(self, s):
        length = 0
        max_s = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                if self.ss(s[i:j+1]):
                    if len(s[i:j+1]) > length:
                        length = len(s[i:j+1])
                        max_s = s[i:j+1]
        return max_s

    def ss(self, s):
        if s == s[::-1]:
            return True
        else:
            return False


if __name__ == '__main__':
    s = input()
    c = Solution()
    print(c.longstPalindrome(s))