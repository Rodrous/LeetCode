class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        current_depth = 1
        if not root:
            return 0
        queue = [root]
        
        while(queue):
            l = len(queue)
            for i in range(l):
                node = queue.pop(0)
                for n in node.children:
                    if n:
                        queue.append(n)
            current_depth +=1
        
        return current_depth-1