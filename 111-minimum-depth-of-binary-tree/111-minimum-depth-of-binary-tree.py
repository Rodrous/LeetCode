# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
 
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        L: int = self.minDepth(root.left)
        R: int = self.minDepth(root.right)
        
        if L == 0 or R == 0:
            return 1 + L + R
        
        return 1 + min(L,R)
        