class Solution:
    def maxArea(self, height: List[int]) -> int:
        ptr_a : int = 0
        ptr_b : int = len(height)-1
        
        result: int = 0 
        
        while ptr_b >= ptr_a:
            area = (ptr_b - ptr_a) * min(height[ptr_a], height[ptr_b])
            result = max(result,area)
            if height[ptr_a] > height[ptr_b]:
                ptr_b -= 1
            else:
                ptr_a += 1
            
        return result