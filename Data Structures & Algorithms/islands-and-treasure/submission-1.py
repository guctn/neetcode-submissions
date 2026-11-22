class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return []

        rows, cols = len(grid), len(grid[0])
        q = collections.deque()
        seen = set()
        INF = 2147483647

        # 01. first we gotta iterate through the entire grid to find all treasure chests
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    q.append((row, col))
                    seen.add((row, col))

        while q:

            curr_row, curr_col = q.popleft()

            directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
            for dr, dc in directions:
                row = curr_row + dr
                col = curr_col + dc
                if 0 <= row < rows and 0 <= col < cols and grid[row][col] not in seen and grid[row][col] == INF:
                    grid[row][col] = grid[curr_row][curr_col] + 1
                    q.append((row, col))
                    seen.add((row, col))

# Time: O(r * c) -> r being row and c bring col | basically we need to iterate through the entire grid to find all treasure chests and then later do a BFS in every level of it which all will the r * c because will iterate at each level and add to the queue each cell equal to INF which is r * c
# Space: O(r * c) because we have a queue which can get the size of r * c (or the number of cells in each level) and also a hash_set which tracks all cells we checked




        