import heapq as hq
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        hq._heapify_max(nums)
        
        nums1 = hq._heappop_max(nums)
        nums2 = hq._heappop_max(nums)
        
        return (nums1-1)*(nums2-1)