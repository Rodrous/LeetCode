class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        posCol = set()
        negCol = set()
        board = [["."]*n for i in range(n)]
        res = []
        def dfs(r):
            
            if n == r:
                res.append(board.copy())
                return
            
            for c in range(n):
                if c in cols or (r+c) in posCol or (r-c) in negCol:
                    continue
                
                cols.add(c)
                posCol.add(r+c)
                negCol.add(r-c)
                
                board[r][c] = "Q"
                dfs(r+1)
                cols.remove(c)
                posCol.remove(r+c)
                negCol.remove(r-c)
                
                board[r][c] = "."
        
        dfs(0)
        return len(res)
                