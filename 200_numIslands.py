# coding: utf-8

# https://leetcode-cn.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        result = 0
        m, n = len(grid), len(grid[0])
        for row in range(m):
            for col in range(n):
                if grid[row][col] == '1':
                    result += 1
                    self._numIslands(grid, row, col)
        return result

    def _numIslands(self, grid, r, c):
        grid[r][c] = '0'
        if 0 < r and grid[r - 1][c] == '1':
            self._numIslands(grid, r - 1, c)

        if 0 < c and grid[r][c - 1] == '1':
            self._numIslands(grid, r, c - 1)

        if c < len(grid[0]) - 1 and grid[r][c + 1] == '1':
            self._numIslands(grid, r, c + 1)

        if r < len(grid) - 1 and grid[r + 1][c] == '1':
            self._numIslands(grid, r + 1, c)


class Solution2:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        result = 0
        m, n = len(grid), len(grid[0])
        for row in range(m):
            for col in range(n):
                if grid[row][col] == '1':
                    result += 1
                    self._numIslands(grid, row, col)
        return result

    def _numIslands(self, grid, r, c):
        grid[r][c] = '0'
        if 0 < r and grid[r - 1][c] == '1':
            self._numIslands(grid, r - 1, c)

        if 0 < c and grid[r][c - 1] == '1':
            self._numIslands(grid, r, c - 1)

        if c < len(grid[0]) - 1 and grid[r][c + 1] == '1':
            self._numIslands(grid, r, c + 1)

        if r < len(grid) - 1 and grid[r + 1][c] == '1':
            self._numIslands(grid, r + 1, c)

    def _numIslands2(self, grid, r, c):
        grid[r][c] = '0'
        if 0 < r and grid[r - 1][c] == '1':
            self._numIslands(grid, r - 1, c)

        if 0 < c and grid[r][c - 1] == '1':
            self._numIslands(grid, r, c - 1)

        if c < len(grid[0]) - 1 and grid[r][c + 1] == '1':
            self._numIslands(grid, r, c + 1)

        if r < len(grid) - 1 and grid[r + 1][c] == '1':
            self._numIslands(grid, r + 1, c)


class Solution3:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.bfs(grid, i, j, m, n)
                    count += 1
        return count

    def bfs(self, grid, i, j, m, n):
        if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == '0' or grid[i][j] == '2':
            return
        grid[i][j] = '2'
        self.bfs(grid, i - 1, j, m, n)
        self.bfs(grid, i + 1, j, m, n)
        self.bfs(grid, i, j - 1, m, n)
        self.bfs(grid, i, j + 1, m, n)


class Solution4:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        from collections import deque
        s = {(i, j) for i, row in enumerate(grid) for j, col in enumerate(row) if col == '1'}
        num = 0
        while s:
            num += 1
            queue = deque([s.pop()])
            while queue:
                i, j = queue.popleft()
                for item in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                    if item in s:
                        s.remove(item)
                        queue.append(item)
        return num


if __name__ == '__main__':
    grid = [
        ['1', '1', '1', '1', '0'],
        ['1', '1', '0', '1', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '0', '1', '0']
    ]
    print(Solution4().numIslands(grid))
