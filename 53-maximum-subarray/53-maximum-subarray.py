class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        
        result: int = -99999
        currentSum: int = 0
        for i in range(len(nums)):
          if currentSum < 0:
            currentSum = nums[i]
          else:
            currentSum += nums[i]
          
          result = max(currentSum,result)
          
        return result