class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        result: int = nums[0] + nums[1] + nums[-1]
        nums.sort()
        
        for i in range(len(nums)-2):
            a_pointer : int = i+1
            b_pointer : int = len(nums)-1
                
            while b_pointer > a_pointer:
                current_sum: int = nums[i] + nums[b_pointer] + nums[a_pointer]
                
                if current_sum > target:
                    b_pointer -= 1
                else:
                    a_pointer += 1
                
                if abs(current_sum - target) < abs(result - target):
                    result = current_sum
        
        return result
        