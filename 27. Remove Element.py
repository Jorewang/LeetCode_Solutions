class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        ret = 0
        for i in nums:
            if i != val:
                nums[ret] = i
                ret += 1
        return ret
