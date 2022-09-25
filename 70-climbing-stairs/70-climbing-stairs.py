class Solution:
    def climbStairs(self, n: int) -> int:
        
        memoryMap = {}
        def drySe(n):
            if n == 0:
                return 1
            
            if n < 0:
                return 0
            
            if n in memoryMap:
                return memoryMap[n]
            
            memoryMap[n] = drySe(n-1) + drySe(n-2)
            
            return memoryMap[n]
            
            
            
        return drySe(n)
