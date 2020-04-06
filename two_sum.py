def two_sum(nums, target):
    lookup = {}
    for i, num in enumerate(nums):
        if target-num in lookup:
            return i, lookup[target-num]
        lookup[num] = i
    return "fail"

if __name__ == '__main__':
    nums = [2,7,11,15]
    print(two_sum(nums,4))