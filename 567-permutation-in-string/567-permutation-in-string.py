class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ptr_a = 0
        ptr_b = len(s1)
        
        while ptr_b <= len(s2):
            if self.checkAnagram(s1,s2[ptr_a:ptr_b]):
                return True
            ptr_a += 1
            ptr_b += 1
        return False
    
    
    def checkAnagram(self,s1,s2) -> bool:
        return collections.Counter(s1) == collections.Counter(s2)