# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import queue
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = queue.Queue()
        q.put(root)
        result: List = []
        while q.qsize():
            level_result: List = []
            for i in range(q.qsize()):
                
                node = q.get()
                if node:
                    q.put(node.left)
                    q.put(node.right)
                    level_result.append(node.val)
                
            if level_result:
                result.append(level_result)
        
        return result
            
        