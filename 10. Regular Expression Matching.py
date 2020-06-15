class Solution(object):
    def isMatch(self, s, p):
        def helper(s, i, p, j):
            if j == -1:
                return i == j
            if i == -1:
                if p[j] != '*':
                    return False
                return helper(s, i, p, j-2)
            if p[j] == '*':
                if p[j-1] == '.' or p[j-1] == s[i]:
                    if helper(s, i-1, p, j):
                        return True
                return helper(s, i, p, j-2)
            if p[j] == '.' or p[j] == s[i]:
                return helper(s, i-1, p, j-1)
            return False
        return helper(s, len(s)-1, p, len(p)-1)

    def dp(self, s, p):
        dp_list = [[0]*(len(p)+1) for _ in range(len(s)+1)]
        dp_list[0][0] = 1
        for j in range(1, len(p)+1):
            if p[j-1] == '*':
                dp_list[0][j] = dp_list[0][j-2]
        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):
                if p[j-1] == '*':
                    if (p[j-2] == '.' or p[j-2] == s[i-1]) and dp_list[i-1][j] == 1:
                        dp_list[i][j] = 1
                        continue
                    dp_list[i][j] = dp_list[i][j-2]
                if p[j-1] == '.' or p[j-1] == s[i-1]:
                    dp_list[i][j] = dp_list[i-1][j-1]
        print(dp_list)
        return dp_list[len(s)][len(p)] == 1


if __name__ == '__main__':
    c = Solution()
    print(c.isMatch('aab', 'b.*'))
    print(c.dp('aab', 'b.*'))
