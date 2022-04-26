import heapq as hq
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k2: int) -> List[int]:
        mat2 = {}
        for i, k in enumerate(mat):
            res = 0
            for j in k:
                if j == 1:
                    res+=1
            mat2[i] = res
        
        
        mat2 = sorted(mat2.items(), key = lambda x: x[1])
        return [mat2[i][0] for i in range(k2)]
        
            
            
        
        