class Solution(object):
    def longestCommonSubstring(self, A, B):
        if not A or not B:
            return 0
        lcs = 0
        for i in range(len(A)):
            for j in range(len(B)):
                lcs_tmp = 0
                while i+lcs_tmp < len(A) and j+lcs_tmp < len(B) and A[i+lcs_tmp] == B[j+lcs_tmp]:
                    lcs_tmp += 1
                if lcs < lcs_tmp:
                    lcs = lcs_tmp
        return lcs

    def longestCommonSubstring_dp(self, A, B):
        if not A or not B:
            return 0
        n = len(A)
        m = len(B)
        f = [[0 for _ in range(m+1)] for _ in range(n+1)]

        for i in range(n):
            for j in range(m):
                if A[i] == B[j]:
                    f[i+1][j+1] = 1+f[i][j]

        lcs = max(map(max, f))
        print(f)
        return lcs


if __name__ == '__main__':
    sa = 'ABCD'
    sb = 'CBCE'

    print(Solution().longestCommonSubstring_dp(sa, sb))
