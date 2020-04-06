
class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        def update(i, j):
            queue = []
            queue.append((i, j))
            visit = [[0 for i in range(col)] for j in range(row)]
            visit[i][j] == 1
            while queue:
                i, j = queue.pop(0)
                if i-1 >= 0:
                    if visit[i-1][j] != 1:
                        if matrix[i-1][j] != 0:
                            if matrix[i-1][j] > matrix[i][j]+1:
                                matrix[i-1][j] = matrix[i][j] + 1
                        visit[i-1][j] = 1
                        queue.append((i-1, j))
                if j+1 <= col-1:
                    if visit[i][j+1] != 1:
                        if matrix[i][j+1] != 0:
                            if matrix[i][j+1] > matrix[i][j]+1:
                                matrix[i][j+1] = matrix[i][j] + 1
                        visit[i][j+1] = 1
                        queue.append((i, j+1))
                if i+1 <= row-1:
                    if visit[i+1][j] != 1:
                        if matrix[i+1][j] != 0:
                            if matrix[i+1][j] > matrix[i][j]+1:
                                matrix[i+1][j] = matrix[i][j] + 1
                        visit[i+1][j] = 1
                        queue.append((i+1, j))
                if j-1 >= 0:
                    if visit[i][j-1] != 1:
                        if matrix[i][j-1] != 0:
                            if matrix[i][j-1] > matrix[i][j]+1:
                                matrix[i][j-1] = matrix[i][j] + 1
                        visit[i][j-1] = 1
                        queue.append((i, j-1))

        row = len(matrix)
        col = len(matrix[0])
        list_0 = []
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    list_0.append((i, j))
                else:
                    matrix[i][j] = 100000
        for i, j in list_0:
            update(i, j)

        return matrix


if __name__ == '__main__':
    m =  [[1,1,1,0,1,0,1,1,1,1,0,0,0,1,1,0,0,0,1,1],[0,1,1,0,1,0,0,0,1,1,1,1,1,1,0,1,0,0,1,0],[0,0,0,1,1,0,1,1,0,0,1,0,1,1,1,0,1,1,0,0],[0,0,1,0,0,0,0,0,1,0,1,1,0,1,0,1,0,0,0,1],[1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,1,1,0,0,0],[1,0,1,0,1,1,0,1,1,0,1,0,1,0,1,0,0,1,0,1],[1,1,1,0,1,0,0,1,1,1,1,1,0,1,1,0,1,1,1,1],[0,1,1,1,0,1,1,1,0,0,0,1,1,1,0,1,0,1,1,1],[1,1,0,1,1,0,0,1,0,0,0,1,1,1,0,0,0,0,1,0],[0,0,1,0,1,1,1,1,0,1,0,0,0,1,0,0,0,0,0,1],[0,0,1,1,1,1,0,0,1,0,1,0,0,1,0,0,0,1,0,0],[1,0,0,1,0,0,1,0,0,1,0,0,0,0,0,1,1,0,1,1],[0,0,1,1,0,0,0,0,1,0,1,0,0,1,0,1,0,0,1,0],[1,0,0,0,1,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0],[1,1,0,1,0,1,0,0,1,1,0,1,0,0,0,0,1,1,1,1],[1,1,1,1,0,1,1,1,0,1,1,1,0,1,0,1,1,0,0,0],[0,1,0,0,0,0,1,0,1,1,0,0,0,0,1,1,0,1,0,0],[0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,1,0,1,0,0],[0,1,1,1,0,0,1,1,1,0,0,1,0,0,1,1,0,1,0,1],[1,0,1,0,1,1,0,0,0,1,0,0,0,0,0,1,1,0,0,1]]

    s = Solution()
    print(s.updateMatrix(m))