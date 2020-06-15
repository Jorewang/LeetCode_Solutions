class Solution(object):
    def addToArrayForm(self, A, K):
        avalue = 0

        for v in A:
            avalue = avalue*10+v

        ans = avalue+K
        if ans == 0:
            return [0]
        li = []
        while ans:
            val = ans % 10
            li.insert(0, val)
            ans = ans // 10
        return li

    def addToArrayForm_2(self, A, K):
        i = len(A) - 1

        while i >= 0 and K > 0:
            temp = A[i] + K%10
            A[i] = temp % 10

            K = K // 10
            K += temp // 10
            i -= 1

        while K > 0:
            A.insert(0, K%10)
            K = K // 10
        return A


if __name__ == '__main__':
    print(Solution().addToArrayForm_2([2, 1, 5], 806))
