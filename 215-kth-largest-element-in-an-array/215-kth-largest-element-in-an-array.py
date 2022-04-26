import heapq as hq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        x: int 
        
        heap = hq._heapify_max(nums)
        while k > 0:
            x = hq._heappop_max(nums)
            k-=1
        return x