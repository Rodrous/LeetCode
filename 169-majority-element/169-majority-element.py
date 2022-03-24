class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        memoryDisc: Dict = {}
        for i in nums:
            if i in memoryDisc:
                memoryDisc[i] +=1
            else:
                memoryDisc[i] = 1
        for i,j in memoryDisc.items():
            if j > int(len(nums)/2):
                return i
        