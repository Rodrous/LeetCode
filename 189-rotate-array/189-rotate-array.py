class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p: int = 0
        q: int = len(nums)-1
        
        while k:
            nums.insert(0,nums[q])
            nums.pop()
            k -=1
        
            