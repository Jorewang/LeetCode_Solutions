def dfs(u, sum, state):
    if sum+n-u < m:
        return
    if sum == m:
        for i in range(n):
            if state >> i & 1:
                print(i + 1, end=" ")
        print()
        return
    dfs(u+1, sum+1, state | 1 << u)
    dfs(u+1, sum, state)


n, m = map(int, input().split())
dfs(0, 0, 0)