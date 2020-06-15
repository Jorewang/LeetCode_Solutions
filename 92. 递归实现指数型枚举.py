def dfs(u, state):
    if u == n:
        for i in range(n):
            if state >> i & 1:
                print(i+1, end=" ")
        print()
        return
    dfs(u+1, state)
    dfs(u+1, state | 1 << u)


n = int(input())
dfs(0, 0)
