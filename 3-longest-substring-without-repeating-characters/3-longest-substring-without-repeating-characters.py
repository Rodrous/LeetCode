class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        memoryDict: Dict = {}
        ptr_a: int = 0
        ptr_b: int = 0
        maxVal: int = 0
        while ptr_b <= len(s)-1:
            if s[ptr_b] not in memoryDict:
                memoryDict[s[ptr_b]] = 1
                maxVal = max(maxVal,len(memoryDict))
                ptr_b += 1
            else:
                
                del memoryDict[s[ptr_a]]
                ptr_a += 1   
            
        return maxVal