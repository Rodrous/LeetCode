# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkSymmetry(self, node_a: Optional[TreeNode], node_b: Optional[TreeNode]) -> bool:
        if not node_a and not node_b:
            return True
        if not node_a or not node_b:
            return False
        if node_a.val != node_b.val:
            return False
        
        return self.checkSymmetry(node_a.left,node_b.right) and self.checkSymmetry(node_a.right, node_b.left) 
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.checkSymmetry(root.left,root.right)
        
        
        