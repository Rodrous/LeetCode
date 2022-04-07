# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import queue as queue
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = queue.Queue()
        q.put(root)
        maxRightNow: List = []
        while q.qsize():
            qLength = q.qsize()
            result: List = []
            for i in range(qLength):
                node = q.get()
                if node:
                    result.append(node.val)
                    q.put(node.left)
                    q.put(node.right)
            if result:
                maxRightNow.append(result)
        return len(maxRightNow)
                    
            
        