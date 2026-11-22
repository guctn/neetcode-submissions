class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1

        rows, cols = len(grid), len(grid[0])
        q = collections.deque()
        number_fruits = 0
        seen = set()
        minutes = 0

        for row in range(rows):         # O(n²)
            for col in range(cols):
                if grid[row][col] == 2:
                    q.append((row, col))
                    seen.add((row, col))
                if grid[row][col] == 1:
                    number_fruits += 1


        while q:
            level_size = len(q)
            fruits_found = 0
            for _ in range(level_size):
                curr_row, curr_col = q.popleft()

                directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
                for dr, dc in directions:
                    row = curr_row + dr
                    col = curr_col + dc

                    if 0 <= row < rows and 0 <= col < cols and (row, col) not in seen and grid[row][col] == 1:
                        q.append((row, col))
                        seen.add((row, col))
                        fruits_found += 1
                        number_fruits -= 1
            
            if fruits_found > 0:
                minutes += 1
                
        if number_fruits > 0 :
            return -1

        return minutes





