# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        slow=head
        fast=head
        #find middle of ll (slow will be at middle)
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        #reverse second half now
        prev=None
        while slow:
            nex=slow.next
            slow.next=prev
            prev=slow
            slow=nex
        #compare first half and second half to check palindronme
        left=head
        right=prev
        while right:  #will stop when right will reach middle
            if left.val!=right.val:
                return False
            left=left.next
            right=right.next
        return True 

        