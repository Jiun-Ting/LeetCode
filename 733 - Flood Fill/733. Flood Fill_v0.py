class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        m, n = len(image), len(image[0])
        Pass = [[False for j in range(n)] for i in range(m)]
        origin = image[sr][sc]
        q = [(sr,sc)]
        image[sr][sc] = newColor
        Pass[sr][sc] = True
        while q:
            vr, vc = q.pop(0)
            image[vr][vc] = newColor
            for (x, y) in [(vr+1, vc), (vr-1, vc), (vr, vc+1), (vr, vc-1)]:
                if x >= 0 and y >= 0 and x < m and y < n and image[x][y] == origin and Pass[x][y]==False:
                    q.append((x, y))
                    image[x][y] = newColor
                    Pass[x][y] = True
        return image
