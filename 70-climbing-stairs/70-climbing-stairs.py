class Solution:
    def climbStairs(self, n: int) -> int:
        
        memoryMap = {}
        def dfs(n):
            if n == 0:
                return 1
            
            if n < 0:
                return 0
            
            if n in memoryMap:
                return memoryMap[n]
            
            memoryMap[n] = dfs(n-1) + dfs(n-2)
            
            return memoryMap[n]
            
            
        print(memoryMap)   
        return dfs(n)
