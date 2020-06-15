class Solution(object):
    def rob(self, nums):

        def helper(nums, i):
            le = len(nums)
            if i == le - 1:
                return nums[le-1]
            if i == le - 2:
                return max(nums[le-1], nums[le-2])
            if i == le - 3:
                return max(nums[le-3] + nums[le-1], nums[le-2])

            return max(helper(nums, i+2) + nums[i], helper(nums, i+1))

        return helper(nums, 0)

    def rob_2(self, nums):
        le = len(nums)
        ans = [0]*(le+1)
        ans[-2] = nums[-1]

        for i in range(le-2, -1, -1):
            ans[i] = max(nums[i] + ans[i+2], ans[i+1])
        return ans[0]


if __name__ == '__main__':
    print(Solution().rob_2([2, 7, 9, 3, 1]))