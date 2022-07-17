class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        memorySet: Set = set(nums)
        longest: int = 0
        for i in nums:
            if i-1 not in memorySet:
                length: int = 0
                while i+length in memorySet:
                    length+= 1
                longest = max(longest,length)
        return longest