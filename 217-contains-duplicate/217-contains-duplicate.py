class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        memory_dict: Dict = {}
        for i in nums:
            if i not in memory_dict:
                memory_dict[i] = 1
            elif i in memory_dict:
                return True
        