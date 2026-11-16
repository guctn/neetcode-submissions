class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        seen = set()
        max_area = 0


        def bfs(row, col): 
            q = collections.deque()
            q.append((row, col))        # q = 
            area = 1                    # area = 1
            seen.add((row, col))        # seen = (0, 1), (0, 2), (1, 2), (2, 2), (2, 1), (3, 1), (1, 0)
            directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if r in range(rows) and c in range(cols) and (r, c) not in seen and grid[r][c] == 1:
                        q.append((r, c))
                        seen.add((r, c))
                        area += 1
            return area



        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and (row, col) not in seen:
                    area = bfs(row, col) # 1, 0
                    max_area = max(max_area, area)

        return max_area
        