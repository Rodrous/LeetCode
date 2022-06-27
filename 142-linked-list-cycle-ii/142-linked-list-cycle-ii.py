# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        vistedNodes: Dict = {}
        pos: int = 0

        
        while curr:
            if curr in vistedNodes:
                return curr
            if curr not in vistedNodes:
                vistedNodes[curr] = "N"
            
            curr = curr.next
            
        
        return None