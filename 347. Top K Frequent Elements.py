from collections import defaultdict
import heapq


class Solution(object):
    def topKFrequet(self, nums, k):
        def f(x):
            nonlocal val_fre
            return val_fre[x]

        val_fre = defaultdict(int)
        for value in nums:
            val_fre[value] += 1
        return heapq.nlargest(k, val_fre, key=f)


if __name__ == '__main__':
    for i in range(3):
        print(i)
    else:
        print("not good")
