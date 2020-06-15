class Solution(object):
    def getPermutation(self, n, k):
        li = [str(x) for x in range(1, n+1)]
        res = []
        def permutation(cur, n):
            if cur == n-1:
                res.append(''.join(li))
            else:
                ne = cur
                while ne < n:
                    li[cur], li[ne] = li[ne], li[cur]
                    permutation(cur+1, n)
                    li[cur], li[ne] = li[ne], li[cur]
                    ne += 1
        permutation(0, n)
        res.sort()
        return res[k-1]

    def getPermutation_2(self, n, k):
        s = ''.join([str(x) for x in range(1, n+1)])
        def permutation(s):
            if len(s) == 0:
                return
            if len(s) == 1:
                return [s]
            res = []
            for i in range(len(s)):
                x = s[i]
                xs = s[:i] + s[i+1:]
                for j in permutation(xs):
                    res.append(x+j)
            return res
        return permutation(s)[k-1]

    def getPermutation_3(self, n, k):
        fac = 1
        li = []
        s = ''.join([str(x) for x in range(1, n+1)])
        for i in range(1, n):
            fac *= i
            li.append(fac)
        index = 0
        res = ''
        while index < n-1:
            val = li.pop()
            ch = k//val - 1 if k % val == 0 else k//val
            res += s[ch]
            s = s.replace(s[ch], '')
            k = k % val
            index += 1
        res += s
        return res


if __name__ == '__main__':
    print(Solution().getPermutation_3(3, 6))
