# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: ListNode | None) -> ListNode | None:
        st=[]
        curr=head
        while curr:
            while st and curr.val>st[-1]:
                st.pop()
            st.append(curr.val)
            curr=curr.next
        
        dummy=ListNode()
        curr=dummy
        for n in st:
            curr.next=ListNode(n)
            curr=curr.next
        return dummy.next

            