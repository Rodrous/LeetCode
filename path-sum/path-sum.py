# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkCount(self,root: Optional[TreeNode], targetSum: int, currentSum:int) -> bool:
        if not root:
            return False
        
        currentSum += root.val
        if not root.left and not root.right:
            return currentSum == targetSum
        
        return self.checkCount(root.left,targetSum,currentSum) or self.checkCount(root.right,targetSum,currentSum) 
         
        
    
    
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.checkCount(root,targetSum,0)
    
        