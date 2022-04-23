# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node: ListNode = ListNode()
        dummyNode = node
        
        p: ListNode = list1
        q: ListNode = list2
        
        
        while p and q:
            if p.val < q.val:
                dummyNode.next = p
                p = p.next
            else:
                dummyNode.next = q
                q = q.next
            dummyNode = dummyNode.next
            
        
        if p:
            dummyNode.next = p
            p = p.next
        if q:
            dummyNode.next = q
            q= q.next
        return node.next