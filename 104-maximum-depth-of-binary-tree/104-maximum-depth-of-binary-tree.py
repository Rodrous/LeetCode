# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import queue
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #Can be done using BFS
        q = queue.Queue()
        q.put(root)
        result = []
        
        while q.qsize():
            dummyResult = []
            
            for i in range(q.qsize()):
                node = q.get()
                if node:
                    dummyResult.append(node.val)
                    q.put(node.left)
                    q.put(node.right)
            if dummyResult:
                result.append(dummyResult)
        return len(result)
       
        
        