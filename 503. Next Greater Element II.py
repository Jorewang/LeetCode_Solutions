class Solution(object):
    def nextGreaterElements(self, nums):
        stack = []
        i = 0
        length = len(nums)
        ans = [-1]*length
        while i < 2*length:
            if not stack or nums[i % length] <= stack[-1][1]:
                stack.append((i % length, nums[i % length]))
                i += 1
                continue
            idx, _ = stack.pop()
            if ans[idx] == -1:
                ans[idx] = nums[i % length]
        return ans


if __name__ == '__main__':
    print(Solution().nextGreaterElements([1, 2, 1]))
