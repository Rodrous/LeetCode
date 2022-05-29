# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        bro: ListNode = ListNode(0)
        dummy = bro
        carry: int = 0
        
        p: Optional[ListNode] = l1
        q: Optional[ListNode] = l2
        
        while p or q:
            x: int = p.val if p != None else 0
            y: int = q.val if q != None else 0
            sumofint = x + y + carry
            carry = sumofint//10
            dummy.next = ListNode(sumofint%10)
            dummy = dummy.next
            
            if p:
                p = p.next
            if q:
                q = q.next
            
            if carry > 0:
                dummy.next = ListNode(carry)
        
        return bro.next