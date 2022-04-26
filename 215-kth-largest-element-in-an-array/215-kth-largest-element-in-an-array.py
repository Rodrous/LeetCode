import heapq as hq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        x: int 
        k = len(nums)-k+1
        heap = hq.heapify(nums)
        while k > 0:
            x = hq.heappop(nums)
            k-=1
        return x