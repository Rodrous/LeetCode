class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        memory = set(nums)
        longest = 0
        
        for i in nums:
            if i - 1 not in memory:
                length = 0
                while i + length in memory:
                    length += 1
                longest = max(longest, length)
        return longest