class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet: Set = set()
        i: int = 0
        result:int = 0
            
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[i])
                i+=1
            charSet.add(s[r])
            result = max(result, r-i +1)
        return result