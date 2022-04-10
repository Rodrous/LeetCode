class Solution:
    def romanToInt(self, s: str) -> int:
        mappingDict: Dict = {
            "I": 1,
            "V": 5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        result = 0
        
        p: int = 0
        
        while p <= len(s)-1:
            if p+1 <= len(s)-1 and mappingDict[s[p]] < mappingDict[s[p+1]]:
                result -= mappingDict[s[p]]
            else:
                result += mappingDict[s[p]]
            p += 1
        
        return result
        
        