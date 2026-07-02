class Solution:

    def floodFill(
        self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        start_color = image[sr][sc]

        if start_color == color:
            return image

        rows, cols = len(image), len(image[0])

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if image[r][c] != start_color:
                return

            image[r][c] = color

            dfs(r + 1, c)  # Down
            dfs(r - 1, c)  # Up
            dfs(r, c + 1)  # Right
            dfs(r, c - 1)  # Left

        dfs(sr, sc)

        return image