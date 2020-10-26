# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        d=ListNode()
        d.next = head
        a=d
        b=d
        for i in range(0,n):
            b= b.next
        while b.next: 
            a=a.next
            b=b.next
        
        a.next = a.next.next
        return d.next
    
