class Solution(object):
    def updateMatrix(self, matrix):
        if not matrix or not matrix[0]:
            return
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]

        def bfs(i, j):
            queue = [(i, j, 0)]

            while queue:
                x, y, dis = queue.pop(0)
                for k in range(4):
                    temp_x = x + dx[k]
                    temp_y = y + dy[k]
                    temp_dis = dis + 1
                    if 0 <= temp_x < len(matrix) and 0 <= temp_y < len(matrix[0]):
                        if matrix[temp_x][temp_y] == 0:
                            return temp_dis
                        queue.append((temp_x, temp_y, temp_dis))

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] != 0:
                    matrix[i][j] = bfs(i, j)
        return matrix


if __name__ == '__main__':
    print(Solution().updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]]))

