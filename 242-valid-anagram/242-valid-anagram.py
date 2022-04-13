class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        frequencyMapper_1: Dict = {}
        frequencyMapper_2: Dict = {}
        
        if len(s) != len(t): return False
        
        for i in s:
            if i in frequencyMapper_1:
                frequencyMapper_1[i] += 1
            else:
                frequencyMapper_1[i] = 1
        
        for j in t:
            if j in frequencyMapper_2:
                frequencyMapper_2[j] += 1
            else:
                frequencyMapper_2[j] = 1
        return frequencyMapper_1 == frequencyMapper_2
    
        