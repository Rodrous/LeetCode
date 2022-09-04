import heapq
class Solution:
    
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq._heapify_max(stones)
        while len(stones) > 1:
            a = heapq._heappop_max(stones)
            b = heapq._heappop_max(stones)

            if a != b:
                new_weight = abs(b - a)
                heapq.heappush(stones,new_weight)
                heapq._heapify_max(stones)

        
        if len(stones) == 0:
            return 0
        return stones[-1]