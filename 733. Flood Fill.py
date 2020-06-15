class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        if not image or not image[0]:
            return

        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]

        oldColor = image[sr][sc]
        if oldColor == newColor:
            return image
        image[sr][sc] = newColor
        for i in range(4):
            x = sr + dx[i]
            y = sc + dy[i]
            if 0 <= x < len(image) and 0 <= y < len(image[0]) and image[x][y] == oldColor:
                self.floodFill(image, x, y, newColor)
        return image
