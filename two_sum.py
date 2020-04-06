def two_sum(nums, target):
    lookup = {}
    for i, num in enumerate(nums):
        if target-num in lookup:
            return i, lookup[target-num]
        lookup[num] = i
    return "fail"

