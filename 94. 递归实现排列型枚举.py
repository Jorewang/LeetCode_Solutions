n = int(input())
path = []


def dfs(u, state):
    if u == n:
        for p in path:
            print(p, end=' ')
        print()

    for i in range(n):
        if not (state >> i & 1):
            path.append(i + 1)
            dfs(u + 1, state | 1 << i)
            path.pop()

dfs(0, 0)

