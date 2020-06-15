class Solution(object):
    def maxWidthRamp(self, A):
        ans = 0
        for i, value in enumerate(A):

            next = i+1
            j = i
            while next < len(A):
                if A[next] >= A[i]:
                    j = next
                next += 1
            if j-i > ans:
                ans = j-i
        return ans

    def maxWidthRamp_2(self, A):
        def f(x):
            return x[1]
        li = []
        for i, value in enumerate(A):
            li.append((value, i))
        li.sort()
        print(li)
        ans = 0
        for i, tup in enumerate(li):
            ans = max(sorted(li[i:], key=f)[-1][1]-tup[1], ans)
        return ans

    def maxWidthRamp_3(self, A):
        s = []

        for i, value in enumerate(A):
            if not s or A[s[-1]] > value:
                s.append(i)
        ans = 0

        for i in range(len(A))[::-1]:
            while s and A[s[-1]] <= A[i]:
                ans = max(ans, i-s.pop())
        return ans


if __name__ == '__main__':
    print(Solution().maxWidthRamp_3([6, 0, 8, 2, 1, 5]))
    print(Solution().maxWidthRamp_3([9, 8, 1, 0, 1, 9, 4, 0, 4, 1]))
