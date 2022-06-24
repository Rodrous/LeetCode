class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_1: Dict = {}
        map_2: Dict = {}
            
        for i,j in zip(s,t):
            if (i not in map_1) and (j not in map_2):
                map_1[i] = j
                map_2[j] = i
            
            elif map_1.get(i)!= j or map_2.get(j) != i:
                return False
        
        return True