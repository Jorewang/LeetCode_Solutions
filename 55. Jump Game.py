class Solution(object):
    def canJump_recur(self, nums):

        def helper(idx):
            if idx == 0:
                return True

            for i in range(idx):
                if nums[i] >= idx - i:
                    if helper(i):
                        return True
            return False

        return helper(len(nums) - 1)

    def canJump_dp(self, nums):
        helper = [False]*len(nums)
        helper[0] = True

        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[j] >= i - j and helper[j]:
                    helper[i] = True

        return helper[-1]

    def canJump_3(self, nums):
        if not nums or len(nums) <= 1:
            return True

        max_jump = 0
        le = len(nums)
        for i in range(le):
            max_jump = max(max_jump - 1, nums[i])
            if i+max_jump >= le - 1:
                return True
            if max_jump <= 0:
                return False

    def canJump_4(self, nums):
        reach = nums[0]
        le = len(nums)
        for i in range(1, le):
            if reach < i:
                return False
            reach = max(reach, i + nums[i])

            if reach >= le - 1:
                return True

if __name__ == '__main__':
    print(Solution().canJump_4([2, 3, 1, 1, 4]))
