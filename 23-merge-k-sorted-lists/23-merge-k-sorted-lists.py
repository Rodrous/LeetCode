# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from queue import PriorityQueue
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes: PriorityQueue = PriorityQueue()
        dummyNode: ListNode = ListNode(0)
        refDummy = dummyNode
        
        
        for node in lists:
            while node:
                nodes.put(node.val)
                node = node.next
        
        while nodes.qsize() != 0:
            dummyNode.next = ListNode(nodes.get())
            dummyNode = dummyNode.next
        
        return refDummy.next
        
            
            
        