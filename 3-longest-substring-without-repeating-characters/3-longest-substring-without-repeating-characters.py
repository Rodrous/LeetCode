class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        memoryDict: Dict = {}
        i: int = 0 
        j: int = 0
        maxValue = 0
        while j <= len(s)-1:
            if s[j] not in memoryDict:
                memoryDict[s[j]] = 1
                maxValue = max(maxValue,len(memoryDict))
                j+=1
            else:
                del memoryDict[s[i]]
                i+=1
        return maxValue
            
            
        
        
        