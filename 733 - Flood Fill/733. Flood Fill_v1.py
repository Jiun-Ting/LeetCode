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
        origin = image[sr][sc]
        if image[sr][sc] != newColor:
            q = collections.deque([(sr,sc)])
            image[sr][sc] = newColor
            while q:
                vr, vc = q.popleft()
                image[vr][vc] = newColor
                for (x, y) in [(vr+1, vc), (vr-1, vc), (vr, vc+1), (vr, vc-1)]:
                    if m > x >= 0 and n > y >= 0 and image[x][y] == origin:
                        q.append((x, y))
                        image[x][y] = newColor
        return image
