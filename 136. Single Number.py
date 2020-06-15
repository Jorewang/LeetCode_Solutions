class Solution(object):
    def singleNumber(self, nums):
        res = 0
        for val in nums:
            res = res ^ val

        return res


if __name__ == '__main__':
    print(Solution().singleNumber([4,1,2,1,2]))
