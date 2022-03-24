class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        resultant: List[List[int]] = []
        for i in range(len(nums)-1):
            targetRn: int = nums[i] * -1
            ptr_a: int = i+1
            ptr_b: int = len(nums)-1
            
            while ptr_b > ptr_a:
                if nums[ptr_a] + nums[ptr_b] > targetRn:
                    ptr_b -= 1
                elif nums[ptr_a] + nums[ptr_b] < targetRn:
                    ptr_a += 1
                elif nums[ptr_a] + nums[ptr_b] == targetRn:
                    if [nums[i], nums[ptr_a],nums[ptr_b]] in resultant:
                        pass
                    else:
                        resultant.append([nums[i], nums[ptr_a],nums[ptr_b]])
                    ptr_a +=1 
                    ptr_b -=1
        return resultant
                    
            
            
        