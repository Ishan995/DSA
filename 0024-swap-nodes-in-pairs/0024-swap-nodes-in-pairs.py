# Definition for singly-linked list.
#class ListNode:
    #def __init__(self, val=0, next=None):
        #self.val = val
        #self.next = next

class Solution:
    def reverse(self, head: ListNode, times: int) -> None:
        curr = head
        prev = None
        while times > 0:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex
            times -= 1
        return

    def swapPairs(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        
        size = 2
        left = head
        right = None
        res = None
        prevleft = None

        while True:
            right = left
            for i in range(size - 1):
                if right == None:
                    break
                right = right.next
            
            if right:  # left right mil chuka hai
                nextleft = right.next
                self.reverse(left, size)
                
                if prevleft:
                    prevleft.next = right
                prevleft = left
                
                if res == None:
                    res = right
                
                left = nextleft
            else:  # khatam hai sb
                if prevleft:
                    prevleft.next = left
                if res == None:
                    res = left
                break

        return res
        