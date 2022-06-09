class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        if len(nums) == 1:
            return [nums[:]]
        
        for i in range(len(nums)):
            n = nums.pop(0)
            permute = self.permute(nums)
            
            for perm in permute:
                perm.append(n)
            result.extend(permute)
            nums.append(n)
        return result