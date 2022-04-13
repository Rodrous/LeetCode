class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        frequencyMapper_1: Dict = {}
        
        
        if len(s) != len(t): return False
        
        for i in s:
            if i in frequencyMapper_1:
                frequencyMapper_1[i] += 1
            else:
                frequencyMapper_1[i] = 1
        
        
        for i in t:
            if i in frequencyMapper_1:
                frequencyMapper_1[i] -=1
                if frequencyMapper_1[i] == 0:
                    del frequencyMapper_1[i]
            
        
        if frequencyMapper_1:
            return False
        return True