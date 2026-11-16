class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        islands = 0
        seen = set()

        def bfs(row, col):
            # sure of grid[0, 0] is "1"
            q = collections.deque()
            q.append((row, col))
            seen.add((row, col))
            directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if (r in range(rows) and c in range(cols) and (r, c) not in seen and  grid[row][col] == '1'):
                        q.append((r, c))
                        seen.add((r,c))
                       


        for r in range(rows):       # 0
            for c in range(cols):   # 0
                if grid[r][c] == "1" and (r, c) not in seen:
                    bfs(r, c)
                    islands += 1
        
        return islands



