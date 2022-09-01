class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        
        for i,v in enumerate(temperatures):
            
            while stack and stack[-1][1] < v:
                stackIn, stackVal = stack.pop()
                res[stackIn] = i - stackIn 
            stack.append((i,v))
            
            
        return res