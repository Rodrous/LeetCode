class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentSum: int = 0
        result: int = nums[0]
        for i in nums:
            if currentSum < 0:
                currentSum = 0
            currentSum += i
            result = max(currentSum, result)
        return result
            