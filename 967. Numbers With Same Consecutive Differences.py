class Solution(object):
    def numsSameConsecDiff(self, N, K):
        ans = []

        def dfs(N, cur):
            if N == 0:
                ans.append(cur)
                return
            if K == 0:
                ans.append(int(str(cur)*(N+1)))
                return
            l = cur % 10
            if l+K <= 9:
                dfs(N-1, cur*10+l+K)
            if l-K >= 0:
                dfs(N-1, cur*10+l-K)

        if N == 1:
            ans.append(0)
        for i in range(1, 10):
            dfs(N-1, i)
        return ans


if __name__ == '__main__':
    print(Solution().numsSameConsecDiff(2, 5))
