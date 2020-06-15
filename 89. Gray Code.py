class Solution(object):
    def grayCode(self, n):

        def helper(n):
            if n == 0:
                return [0]
            if n == 1:
                return [0, 1]
            part1 = helper(n-1)
            part2 = list(map(lambda k: k + 3*pow(2, n-2), part1[:pow(2, n-1)//2]))
            part3 = list(map(lambda k: k + pow(2, n-2), part1[pow(2, n-1)//2:]))

            return part1 + part2 + part3
        return helper(n)

    def grayCode_2(self, n):

        res = [(i >> 1) ^ i for i in range(pow(2, n))]
        return res


if __name__ == '__main__':
    for i in range(20):
        if Solution().grayCode(i) != Solution().grayCode_2(i):
            print("fuck")
            break
    else:
        print("ok")
