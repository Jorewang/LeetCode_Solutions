class Solution(object):
    def lengthOfLongestSubstring(self, s):
        max = 0
        for t, i in enumerate(s):
            ls = {i: 0}
            sum = 1
            for a in s[t+1:]:
                if a not in ls:
                    sum = sum+1
                    ls[a] = 0
                else:
                    if sum > max:
                        max = sum
                    break
            if sum > max:
                max = sum

        return max

s = input()
sl = Solution()
print(sl.lengthOfLongestSubstring(s))