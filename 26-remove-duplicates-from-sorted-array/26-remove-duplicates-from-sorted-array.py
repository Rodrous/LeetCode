class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        alreadySeen: int | None = None
        k = 0
        for i , j in enumerate(nums):
            if j == alreadySeen:
                nums[i] = 101
            else:
                alreadySeen = j
                k+=1
        nums.sort()
        return k
        