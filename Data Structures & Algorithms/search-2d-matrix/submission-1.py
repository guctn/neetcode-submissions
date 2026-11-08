class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        for row in range(rows):
            left, right = 0, cols - 1
            while (matrix[row][0] <= target and matrix[row][-1] >= target) and left <= right:
                middle = (left + right) // 2

                if matrix[row][middle] == target:
                    return True
                elif target > matrix[row][middle]:
                    left = middle + 1
                else:
                    right = middle - 1
        return False
        