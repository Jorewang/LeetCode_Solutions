class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        pre = nums[0]
        count = 1
        for i, val in enumerate(nums[1:]):
            if pre != val:
                nums[count] = val
                count += 1
                pre = val
        return count


