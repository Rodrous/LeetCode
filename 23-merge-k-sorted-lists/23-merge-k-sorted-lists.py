# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes: List = []
        dummyNode: ListNode = ListNode(0)
        refDummy = dummyNode
        
        
        for node in lists:
            while node:
                nodes.append(node.val)
                node = node.next
        
        for i in sorted(nodes):
            dummyNode.next = ListNode(i)
            dummyNode = dummyNode.next
        
        
        return refDummy.next
            
            
        