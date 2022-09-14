class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        sol = 0
        def dfs(r,c):
            
            if r < 0 or c < 0 or r+1 > rows or c + 1 > cols or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            return 1 + dfs(r-1,c) + dfs(r+1,c) + dfs(r,c-1) + dfs(r,c+1)
        
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    sol = max(dfs(i,j), sol)
        
        return sol