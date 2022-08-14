# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nodeList = []
        
        def fillNode(root):
            if not root:
                
                return 
            
            fillNode(root.left)
            fillNode(root.right)
            
            nodeList.append(root.val)
        
        fillNode(root)
        nodeList.sort()
        return nodeList[k-1]
        