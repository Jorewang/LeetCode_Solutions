import math
import random


class Solution(object):
    def numSquares(self, n):

        def helper(i, target):
            if target == 0 and i >= 0:
                return 0
            if target < 0:
                return 1000
            if i == 0:
                return 1000
            return min(helper(i, target-i**2) + 1, helper(i-1, target))
        return helper(math.floor(math.sqrt(n)), n)

    def numSquares_2(self, n):

        i, j = n+1, math.floor(math.sqrt(n))+1
        dp = [[-1]*j for _ in range(i)]
        for t in range(j):
            dp[0][t] = 0
        for t in range(1, i):
            for k in range(1, j):
                if t-k**2 < 0:
                    dp[t][k] = dp[t][k-1]
                else:
                    if dp[t-k**2][k] != -1 and dp[t][k-1] != -1:
                        dp[t][k] = min(dp[t-k**2][k] + 1, dp[t][k-1])
                    elif dp[t-k**2][k] == -1:
                        dp[t][k] = dp[t][k-1]
                    else:
                        dp[t][k] = dp[t-k**2][k] + 1
        return dp[-1][-1]

    def numSquares_3(self, n):
        q = []
        visit = [0]*(n+1)
        q.append((n, 0))
        visit[n] = 1

        while q:
            num, step = q.pop(0)

            i = 1
            t = num - i**2
            while t >= 0:
                if t == 0:
                    return step + 1

                if visit[t] == 0:
                    q.append((t, step+1))
                    visit[t] = 1
                i += 1
                t = num - i**2


if __name__ == '__main__':
    for _ in range(1000):
        n = random.randint(1, 444)
        if Solution().numSquares_2(n) != Solution().numSquares_3(n):
            print(n)
            print("Shit")
            break
    else:
        print("Done")
