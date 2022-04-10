# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,root: Optional[TreeNode]) -> List:
        if not root:
            return [True, 0]
        left: TreeNode = self.dfs(root.left)
        right: TreeNode = self.dfs(root.right)
        
        result = left[0] and right[0] and abs(right[1]-left[1]) <=1
        
        return [result, max(left[1],right[1])+1]
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root)[0]