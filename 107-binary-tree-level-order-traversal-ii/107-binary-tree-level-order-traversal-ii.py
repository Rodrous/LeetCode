# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import queue as queue
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = queue.Queue()
        q.put(root)
        resultant: List = []
        
        while q.qsize():
            qlength = q.qsize()
            
            tempResult: List = []
            for i in range(qlength):
                node = q.get()
                if node:
                    tempResult.append(node.val)
                    q.put(node.left)
                    q.put(node.right)
            
            if tempResult:
                resultant.append(tempResult)
        
        return resultant[::-1]
        