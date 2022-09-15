class Solution:
    def solve(self, grid: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(grid),len(grid[0])
        
        def dfs(r,c):
            
            if r < 0 or c < 0 or r == rows or c == cols or grid[r][c] != "O":
                return 
            
            grid[r][c] = "C"
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c-1)
            dfs(r,c+1)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "O" and (i in [0,rows-1] or j in [0,cols-1]):
                    dfs(i,j)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "O":
                    grid[r][c] = "X"
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "C":
                    grid[r][c] = "O"
        return grid