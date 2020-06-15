class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False

        n = len(matrix)
        m = len(matrix[0])
        l, r = 0, n*m-1

        while l < r:
            mid = l + r >> 1
            if matrix[mid / m][mid % m] >= target:
                r = mid
            else:
                l = mid + 1
        return matrix[r / m][r % m] == target
