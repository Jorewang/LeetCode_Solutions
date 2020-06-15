class Solution(object):
    def isPalindrome(self, s):
        res = []
        for char in s:
            if char.isalnum():
                res.append(char.lower())
        return res == res[::-1]

    def isPalindrome_2(self, s):
        if not s:
            return True

        l, r = 0, len(s)-1

        while l < r:
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue
            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False
        return True


if __name__ == '__main__':
    s = "A man, a plan, a canal: Panama"
    print(Solution().isPalindrome(s))
