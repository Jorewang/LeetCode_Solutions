class Solution(object):
    def rotateString(self, A, offset):
        if offset == 0:
            return A
        s = list(A)
        c = 0
        length = len(s)
        while c < length:
            k = offset*(c+1) % length
            s[0], s[k] = s[k], s[0]
            c += 1
        return ''.join(s)

    def rotateString_2(self, A, offset):
        if offset == 0:
            return A

        offset %= len(A)
        before = A[:len(A)-offset]
        after = A[len(A)-offset:]

        A = before[::-1] + after[::-1]
        A = A[::-1]

        return A

    def rotateString_3(self, A, B):
        if len(A) != len(B):
            return False
        for sli in range(len(A)):
            print(A[:sli])
            print(B[-(sli):])
            print(A[sli:])
            print(B[:-(sli)])
            if A[:sli] == B[-(sli):] and A[sli:] == B[:-(sli)]:
                return True
        return False


if __name__ == '__main__':
    A = ''
    B = ''
    print(Solution().rotateString_3(A, B))

