# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.solution = 0
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.calculateDepth(root,1)
        return self.solution
    def calculateDepth(self,root: Optional[TreeNode],depthRightNow:int ):
        if root:
            self.solution = max(self.solution,depthRightNow)
            self.calculateDepth(root.left, depthRightNow+1)
            self.calculateDepth(root.right, depthRightNow+1)
        
        