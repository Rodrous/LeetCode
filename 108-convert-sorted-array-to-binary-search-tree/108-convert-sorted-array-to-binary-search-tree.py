# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if nums:
            return self.ConvertToTree(nums,0,len(nums)-1)
    
    def ConvertToTree(self,array: List,left: int ,right: int ) -> Optional[TreeNode]:
        if left > right:
            return None
        else:
            midpoint = (left + right) // 2
            node = TreeNode(array[midpoint])
            node.left = self.ConvertToTree(array,left,midpoint-1)
            node.right = self.ConvertToTree(array,midpoint+1,right)
            return node
        
        