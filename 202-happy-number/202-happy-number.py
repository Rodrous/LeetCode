class Solution:
    def sumofSquares(self,digit: int) -> int:
        result: int = 0
        
        while digit/10 > 0:
            value = digit%10
            result += value**2
            digit = digit//10
        
        return result
        
    def isHappy(self, n: int) -> bool:
        seen: set = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = self.sumofSquares(n)
        return n == 1