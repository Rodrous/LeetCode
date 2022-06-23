class Solution:
    def reverse(self, x: int) -> int:
        solution: int = 0
        isNegative: bool = False
        
        if x < 0:
            isNegative = True
            x = x*-1
    
        while x != 0:
            solution = solution * 10 + x%10
            x //= 10
        
        if isNegative:
            solution = solution* -1
        
        if solution >= 2**31 or solution <=  -2**31:
            return 0
        
        return solution
        