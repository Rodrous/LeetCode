# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        import queue as queue
        q = queue.Queue()
        q.put(root)
        
        result: List = []
        
        while q.qsize():
            queueLength = q.qsize()
            levelResult = []
            for i in range(queueLength):
                node = q.get()
                if node:
                    levelResult.append(node.val)
                    q.put(node.left)
                    q.put(node.right)
            if levelResult:
                result.append(levelResult)
        
        return result