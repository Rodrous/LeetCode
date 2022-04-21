# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p: ListNode = headA
        q: ListNode = headB
            
        while p != q:
            if p is None:
                p = headB
            else:
                p = p.next
            
            if q is None:
                q = headA
            else:
                q = q.next
        
        return p
        
        