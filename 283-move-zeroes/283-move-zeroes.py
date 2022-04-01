class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p: int = 0
        q: int = 0
        
        while q <= len(nums)-1:
            if nums[q] != 0:
                nums[q], nums[p] = nums[p],nums[q]
                p+=1
            q+=1