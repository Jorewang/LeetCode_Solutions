from collections import defaultdict


class Solution(object):
    def compareStrings(self, A, B):
        letters = defaultdict(int)
        for a in A:
            letters[a] += 1

        for b in B:
            letters[b] -= 1
            if letters[b] < 0:
                return False

        return True
