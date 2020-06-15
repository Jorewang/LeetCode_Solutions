class Solution(object):
    def longestPalindrome(self, s):
        pass

    def manacher(self, s):
        li = []
        for char in s:
            li.append('#')
            li.append(char)
        li.append('#')
        print(li)
        length = len(li)
        res = [0]*length
        mx, id = -1, -1
        for i in range(length):
            if mx > i and 2*id-i-res[2*id-i]+1 != 0:
               res[i] = min(res[2*id-i], mx-i+1)
            else:
                cot = 1
                while i+cot < length and i-cot >= 0 and li[i+cot] == li[i-cot]:
                    cot += 1
                res[i] = cot
                id = i
                mx = id + res[id] - 1
        return res


if __name__ == '__main__':
    s = '122122'
    s2 = 'abbaTNTabcba'
    print(Solution().manacher(s))
