import random


class Solution(object):
    def canPartitionKSubsets(self, nums, k):

        def dfs(nums, target, num, k):
            if k == 0:
                return True
            for i in range(len(nums)):
                new_nums = nums[:i] + nums[i+1:]
                if num + nums[i] == target:
                    if dfs(new_nums, target, 0, k-1):
                        return True
                elif num + nums[i] < target:
                    if dfs(new_nums, target, num+nums[i], k):
                        return True
                elif num == 0:
                    return False
            return False

        if sum(nums) % k != 0:
            return False
        nums.sort(reverse=True)
        return dfs(nums, sum(nums)/k, 0, k)

    def canPartitionKSubsets_2(self, nums, k):

        visit = [0]*len(nums)

        def helper(nums, target, cur_num, k):
            if k == 0:
                return True
            if cur_num == target:
                return helper(nums, target, 0, k-1)
            if cur_num > target:
                return False
            for i in range(len(nums)):
                if visit[i] == 0:
                    visit[i] = 1
                    if helper(nums, target, cur_num+nums[i], k):
                        return True
                    visit[i] = 0
            return False

        if sum(nums) % k != 0:
            return False
        return helper(nums, sum(nums)/k, 0, k)


if __name__ == '__main__':
    for i in range(1000000):
        k = random.randint(1, 16)
        li = [random.randint(1, 9999) for _ in range(k)]
        print(i)
        if Solution().canPartitionKSubsets(li, k) != Solution().canPartitionKSubsets_2(li, k):
            print("shit")
            break
    else:
        print("done")

