# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.memoryMap = {}
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.fillMemoryMap(root)
        maxCount: int = max(self.memoryMap.values())
        result: List = []
        
        for key,value in self.memoryMap.items():
            if value == maxCount:
                result.append(key)
        return result
    
    
    def fillMemoryMap(self,root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            if root.val not in self.memoryMap:
                self.memoryMap[root.val] = 1
            
            self.memoryMap[root.val] +=1
            
            self.fillMemoryMap(root.left)
            self.fillMemoryMap(root.right)
        