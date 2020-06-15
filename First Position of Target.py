class Solution(object):
    def bs(self, nums, target):
        if not nums:
            return -1

        start = -1
        end = len(nums)

        while start + 1 < end:
            mid = start + (end - start)//2
            if nums[mid] < target:
                start = mid
            else:
                end = mid
        if end == len(nums) or nums[end] != target:
            return -1
        else:
            return end


if __name__ == '__main__':
   test = [1, 2, 3, 3, 4, 5, 10]
   print(Solution().bs(test, 4))
