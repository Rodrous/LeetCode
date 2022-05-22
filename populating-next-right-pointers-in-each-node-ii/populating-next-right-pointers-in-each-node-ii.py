"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
import queue
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        #Do bfs and update the last one to Null
        q = queue.Queue()
        q.put(root)
        while q.qsize():
            tempArray = []
            for i in range(q.qsize()):
                node = q.get()
                if node:
                    tempArray.append(node)
                    q.put(node.left)
                    q.put(node.right)
            
            for i in range(len(tempArray)-1):
                if i != len(tempArray)-1:
                    tempArray[i].next = tempArray[i+1]
                else:
                    tempArray[i+1].next = None
        return root
                
                
        