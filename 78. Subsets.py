class Solution(object):
    def subsets(self, nums):
        res = []
        tmp = []
        def helper(n):
            if n == len(nums):
                res.append(tmp.copy())
                return
            helper(n+1)
            tmp.append(nums[n])
            helper(n+1)
            tmp.pop()

        helper(0)
        return res


if __name__ == '__main__':
    print(Solution().subsets([1, 2, 3, 4]))
