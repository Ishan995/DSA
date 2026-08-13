# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        dummy=ListNode(0,head)

        #reach till left node (phase 1)

        leftPrev,curr=dummy,head
        for i in range(left-1):
            leftPrev=curr
            curr=curr.next

        #now reverse nodes in between left and right
        prev=None
        for i in range(right-left+1):
            nex=curr.next
            curr.next=prev
            prev=curr
            curr=nex

        #update the pointers

        leftPrev.next.next=curr #curr is at the place of node after right node
        leftPrev.next=prev

        return dummy.next





        
        