class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS  = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        
        def dfs(r,c,visit,prevheight):
            if (r <0 or c < 0 or r == ROWS or c == COLS or (r,c) in visit or heights[r][c] <prevheight):
                return None
            visit.add((r,c))
            dfs(r+1,c, visit, heights[r][c])
            dfs(r-1,c, visit, heights[r][c])
            dfs(r,c+1, visit, heights[r][c])
            dfs(r,c-1, visit, heights[r][c])
        
        for r in range(ROWS):
            dfs(r,0,pacific,heights[r][0])
            dfs(r,COLS-1,atlantic,heights[r][COLS-1])
        
        for c in range(COLS):
            dfs(0, c, pacific, heights[0][c])
            dfs(ROWS - 1, c, atlantic, heights[ROWS - 1][c])
        
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r,c])
        
        return res