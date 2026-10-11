# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        #find middle 
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        #reverse seconf half
        prev=None
        curr=slow.next
        slow.next=None #cut the connection between first half and second half (slow is on the middle element where middle elemnt belongs to first part)
        while curr:
            nex=curr.next
            curr.next=prev
            prev=curr
            curr=nex
        #merging two halves
        first=head
        second=prev#second is last elemnt in original list
        while second:
            tmp1=first.next#storing next node before cutting connection\
            tmp2=second.next
            first.next=second
            second.next=tmp1
            first=tmp1#first ko aage badhao
            second=tmp2#second ko aage badhao
            

            


       

        


 
        