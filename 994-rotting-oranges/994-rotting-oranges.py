import queue
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #BFS
        
        fresh,time = 0,0
        rows, cols = len(grid), len(grid[0])
        q = collections.deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append([i,j])
        cordinates = [
            [-1,0], [1,0],[0,-1],[0,1]
        ]
        while q and fresh > 0:
            for i in range(len(q)):
                r,c = q.popleft()
                
                for dr,dc in cordinates:
                    
                    row,col = dr + r, dc + c
                    
                    if (row in range(rows) and col in range(cols) and grid[row][col]==1):
                        grid[row][col] = 2
                        q.append([row,col])
                        fresh -= 1
            time +=  1
        
        
        return time if fresh == 0 else -1
            
        
        