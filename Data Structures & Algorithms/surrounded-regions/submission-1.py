class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # 01. try to map all the O in the edges

        size = len(board[0])
        self.rows, self.cols = len(board), len(board[0]) 

        def dfs(row, col):
            if  row >= self.rows or row < 0 or col >= self.cols or col < 0 or board[row][col] != 'O':
                return
            
            board[row][col] = 'S'
            
            dfs(row+1, col)
            dfs(row, col+1)
            dfs(row-1, col)
            dfs(row, col-1)

        for row in range(self.rows):
            dfs(row, 0)
            dfs(row, self.cols-1)
        
        for col in range(self.cols):
            dfs(0, col)
            dfs(self.rows-1, col)

        
        for row in range(self.rows):
            for col in range(self.cols):
                if board[row][col] == "O":
                    board[row][col] = "X"
                if board[row][col] == "S":
                    board[row][col] = "O"

