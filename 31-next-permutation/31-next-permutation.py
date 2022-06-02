class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        #find a pivot point
        pivot: int = 0
        
        for i in range(len(nums)-1,0,-1):
            if nums[i-1] < nums[i]:
                pivot = i
                break
        
        if pivot == 0:
            nums.sort()
            return 
        
        #Find the first number > pivot
        swap:int = len(nums)-1
        
        while nums[pivot-1] >= nums[swap]:
            swap -=1
        
        #swap
        
        nums[swap],nums[pivot-1] = nums[pivot-1] , nums[swap]
        
        nums[pivot:] = sorted(nums[pivot:])