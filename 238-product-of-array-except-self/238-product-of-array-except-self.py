class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_arr: List = [1]
        postfix_arr: List = [1]
        
        result: List = []
        
        
        for i in range(1,len(nums)):
            prefix_arr.append(prefix_arr[i-1]*nums[i-1])
        
        array = nums[::-1]
        for i in range(1,len(array)):
            postfix_arr.append(array[i-1]*postfix_arr[i-1])
        
        postfix_arr = postfix_arr[::-1]
        
        for i in range(len(prefix_arr)):
            result.append(prefix_arr[i]*postfix_arr[i])
        
        return result