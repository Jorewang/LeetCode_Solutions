class Solution(object):
    def reverseWords(self, s):
        li = s.split(' ')
        res = []
        for i in li:
            if i:
                res.insert(0, i)
        return ' '.join(res)


if __name__ == '__main__':
    s = 'the sky is   blue'
    print(Solution().reverseWords(s))

