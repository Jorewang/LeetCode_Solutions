class Solution(object):
    def rotate(self, nums, k):
        nums[:] = nums[-k:] + nums[:-k]
        return nums

    def rotate_2(self, nums, k):
        le = len(nums)
        startPos = 0
        doneCount = 0
        while doneCount < le:
            nextPos = (startPos+k) % le
            doneCount += 1
            while startPos != nextPos:
                nums[startPos], nums[nextPos] = nums[nextPos], nums[startPos]
                nextPos = (nextPos+k) % le
                doneCount += 1
            startPos = (startPos+1) % le
        return nums

    def rotate_3(self, nums, k):
        le = len(nums)
        def res(i, j, nums):

            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        res(0, le-k-1, nums)
        res(le-k, le-1, nums)
        res(0, le-1, nums)
        return nums


if __name__ == '__main__':
    print(Solution().rotate([1, 2, 3, 4, 5, 6], 2))
    print(Solution().rotate_2([1, 2, 3, 4, 5, 6], 2))
    print(Solution().rotate_3([1, 2, 3, 4, 5, 6], 2))
