class Solution(object):
    def removeDuplicates(self, nums):
        """
        给定一个排序数组，
        你需要在原地删除重复出现的元素，
        使得每个元素只出现一次，
        返回移除后数组的新长度。
        不要使用额外的数组空间，
        你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
        """
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


if __name__ == '__main__':
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    s = Solution()
    print(s.removeDuplicates(nums))
    print(nums)

