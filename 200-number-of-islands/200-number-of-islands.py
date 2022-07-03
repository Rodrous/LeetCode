class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        result: int = 0
        rows: int = len(grid)
        cols: int = len(grid[0])
            
        def dfs(r: int , c: int) -> None:
            if grid[r][c] == "0":
                return None
            
            grid[r][c] = "0"
            if r >= 1:
                dfs(r-1,c)
            if r+1 < rows:
                dfs(r+1,c)
            if c >= 1:
                dfs(r,c-1)
            if c+1 < cols:
                dfs(r,c+1)
                
        
        for i in range(len(grid)):
            for j in range(cols):
                if grid[i][j] == "1":
                    result += 1
                    dfs(i,j)
        
        
        return result
                