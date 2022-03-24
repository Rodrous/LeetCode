class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        memoryDisc: Dict = {}
        for i in nums:
            if i not in memoryDisc:
                memoryDisc[i] = 1
            elif i in memoryDisc:
                memoryDisc[i] += 1
        
        for i,j in memoryDisc.items():
            if j > 1:
                pass
            else:
                return i