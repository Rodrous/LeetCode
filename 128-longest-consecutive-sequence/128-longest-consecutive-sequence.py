class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        longest: int = 1
        current: int = 1
        for i in range(1, len(nums)):
            
            if nums[i-1] != nums[i]:
                if nums[i] == nums[i-1] + 1:
                    current += 1
                else:
                    longest = max(current,longest)
                    current = 1
        
        return max(longest,current)
                    