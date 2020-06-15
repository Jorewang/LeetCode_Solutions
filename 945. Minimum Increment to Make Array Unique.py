class Solution(object):
    def minIncrementForUnique(self, A):
        if not A or len(A) == 0:
            return 0
        A.sort()
        res = 0

        for i in range(1, len(A)):
            if A[i] <= A[i-1]:
                res += A[i-1] - A[i] + 1
                A[i] = A[i-1] + 1

        return res


if __name__ == '__main__':
    print(Solution().minIncrementForUnique([3, 2, 1, 2, 1, 7]))