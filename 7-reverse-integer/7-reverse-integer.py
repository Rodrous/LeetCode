class Solution:
    def reverse(self, x: int) -> int:
        temp = x
        max_u32 = 2 ** 31
        min_u32 = max_u32 * -1
        rev: int = 0
        if x <0 :
            x = x*-1
                
        while x!=0:
            pop: int = x % 10
            x //= 10
            rev = rev * 10 + pop
            
        if temp < 0:
            rev = rev * -1
            
        if rev >= max_u32 or rev <= min_u32:
            return 0
        return rev
        