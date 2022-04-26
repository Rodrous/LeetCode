import heapq as hq
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k2: int) -> List[int]:
        mat2 = {}
        for i, k in enumerate(mat):
            mat2[i] = sum(k)
        
        return [i[0] for i in sorted(mat2.items(), key= lambda x: x[1])][:k2]
        
        
      
            
            
        
        