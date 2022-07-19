class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        memorymap: Dict = {}
        l: int = 0
        maxf: int = 0
        result: int = 0
            
        for r,val in enumerate(s):
            memorymap[val] = 1 + memorymap.get(val,0)
            maxf = max(memorymap[val],maxf)
            
            if (r-l+1) - maxf > k:
                
                memorymap[s[l]] -= 1
                l+=1
            
            result = max(result,r-l+1)
        return result