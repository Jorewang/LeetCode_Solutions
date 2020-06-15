from collections import Counter


class Solution(object):
    def isAnagram(self, s, t):
        return Counter(s) == Counter(t)


if __name__ == '__main__':
    print(Solution().isAnagram('a', 'b'))
