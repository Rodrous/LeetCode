# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None
        rootNode = TreeNode(postorder.pop())
        midpoint = inorder.index(rootNode.val)
        rootNode.right = self.buildTree(inorder[midpoint+1:],postorder)
        rootNode.left = self.buildTree(inorder[:midpoint], postorder)
        
        return rootNode
        
        