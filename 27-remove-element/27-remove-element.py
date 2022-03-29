class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i: int = 0
        j: int = len(nums)-1
        
        while j >= i:
            if nums[i] != val:
                i+=1
            else:
                nums[i], nums[j] = nums[j],nums[i]
                nums[j] = "_"
                j-=1
            
        value = 0
        for i in nums:
            if i != "_":
                value +=1
        return value