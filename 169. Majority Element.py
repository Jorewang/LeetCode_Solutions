class Solution(object):
    def majorityElement(self, nums):
        nums.sort()
        le = len(nums)
        val = nums[0]
        count = 0
        for i in nums:
            if i != val:
                if count > le // 2:
                    return val
                else:
                    count = 1
                    val = i
            else:
                count += 1
                if count > le // 2:
                    return val

    def majorityElement2(self, nums):
        d = {}
        le = len(nums)
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
            if d[i] > le//2:
                return i


if __name__ == '__main__':
    print(Solution().majorityElement2([2, 2, 1, 1, 1, 2, 2]))

