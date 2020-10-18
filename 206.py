# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev=None
        n=head
        while n!=None:
            
            tmp=n.next
            n.next=prev
            prev=n
            n=tmp
            
        return(prev)
            
            
