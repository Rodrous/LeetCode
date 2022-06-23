class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total: int = sum(nums)
        leftSum: int = 0
        for j,i in enumerate(nums):
            if leftSum == total-leftSum-i:
                return j
            leftSum += i
        return -1
            