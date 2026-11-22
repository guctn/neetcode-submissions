class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return []

        rows, cols = len(grid), len(grid[0])
        q = collections.deque()
        seen = set()
        land_number = 0
        INF = 2147483647

        # 01. first we gotta iterate through the entire grid to find all treasure chests
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    q.append((row, col))
                    seen.add((row, col))

        while q:
            level_size = len(q)

            for _ in range(level_size):
                curr_row, curr_col = q.popleft()

                directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
                for dr, dc in directions:
                    row = curr_row + dr
                    col = curr_col + dc
                    if 0 <= row < rows and 0 <= col < cols and grid[row][col] not in seen and grid[row][col] == INF:
                        grid[row][col] = grid[curr_row][curr_col] + 1
                        q.append((row, col))
                        seen.add((row, col))






        