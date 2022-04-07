# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import queue as queue
from statistics import mean
class Solution:
    
    
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = queue.Queue()
        q.put(root)
        result: List = []
        while q.qsize():
            qLength = q.qsize()
            additiongoBrr: List = []
            for i in range(qLength):
                node = q.get()
                if node:
                    additiongoBrr.append(node.val)
                    q.put(node.left)
                    q.put(node.right)
            if additiongoBrr:
                result.append(mean(additiongoBrr))
        
        return result
                