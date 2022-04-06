class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        windowSize = len(s1)
        start = 0
        if len(s1) > len(s2):
            return False
        
        while (start + windowSize) <= len(s2):
            if self.isAnagram(s2[start:start+windowSize], s1):
                return True
            start = start + 1
        
        return False
    
    def isAnagram(self, s1, s2):
        s1Map = {}
        
        for ch in s1:
            if ch in s1Map:
                s1Map[ch] +=1
            else:
                s1Map[ch] = 1
        
        for ch in s2:
            if ch in s1Map:
                s1Map[ch] -=1
        
        for k,v in s1Map.items():
            if v != 0:
                return False
            
        return True
                   