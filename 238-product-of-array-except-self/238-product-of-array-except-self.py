import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_array: List = [1]
        postfix_array: List = [1]
        output_array: List = []
        
        for i in range(1,len(nums)):
            prefix_array.append(nums[i-1]*prefix_array[i-1])
        
        array = nums[::-1]
        
        for i in range(1,len(array)):
            postfix_array.append(array[i-1]*postfix_array[i-1])
        
        
        postfix_array = postfix_array[::-1]
        
        for i in range(len(postfix_array)):
            output_array.append(postfix_array[i]*prefix_array[i])
        
        return output_array
        
        