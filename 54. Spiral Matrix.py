class Solution(object):
    def spiralOrder(self, matrix):
        if not matrix or not matrix[0]:
            return []
        res = []
        def helper(x1, y1, x2, y2):
            if x1 > x2 or y1 > y2:
                return
            if x1 == x2 and y1 == y2:
                res.append(matrix[x1][y1])
                return
            if x1 == x2:
                for i in range(y1, y2+1):
                    res.append(matrix[x1][i])
                return
            if y1 == y2:
                for i in range(x1, x2+1):
                    res.append(matrix[i][y1])
                return
            for i in range(y1, y2):
                res.append(matrix[x1][i])
            for i in range(x1, x2):
                res.append(matrix[i][y2])
            for i in reversed(range(y1+1, y2+1)):
                res.append(matrix[x2][i])
            for i in reversed(range(x1+1, x2+1)):
                res.append(matrix[i][y1])
            helper(x1+1, y1+1, x2-1, y2-1)

        helper(0, 0, len(matrix)-1, len(matrix[0])-1)

        return res


    def spiralOrder_2(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == [] : return []
        res = []
        maxUp = maxLeft = 0
        maxDown = len(matrix) - 1
        maxRight = len(matrix[0]) - 1
        direction = 0 # 0 go right, 1 go down, 2 go left, 3 up
        while True:
            if direction == 0:
                for i in range(maxLeft, maxRight+1):
                    res.append(matrix[maxUp][i])
                maxUp += 1
                print(res)
            elif direction == 1:
                for i in range(maxUp, maxDown+1):
                    res.append(matrix[i][maxRight])
                maxRight -= 1
                print(res)
            elif direction == 2:
                for i in reversed(range(maxLeft, maxRight+1)):
                    res.append(matrix[maxDown][i])
                maxDown -= 1
            else:
                for i in reversed(range(maxUp, maxDown+1)):
                    res.append(matrix[i][maxLeft])
                maxLeft += 1
            if maxUp > maxDown or maxLeft > maxRight:
                return res
            direction = (direction + 1) % 4


if __name__ == '__main__':
    print(Solution().spiralOrder_2([[1, 2, 3],
                                    [4, 5, 6],
                                    [7, 8, 9]]))

