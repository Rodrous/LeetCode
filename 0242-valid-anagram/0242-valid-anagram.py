
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        obj1: Counter = Counter(s)
        obj2: Counter = Counter(t)
            
        for i in obj1.keys():
            if obj2.get(i) and obj2.get(i) == obj1.get(i):
                continue
            else:
                return False
        
        for i in obj2.keys():
            if obj2.get(i) and obj2.get(i) == obj1.get(i):
                continue
            else:
                return False
        return True
        