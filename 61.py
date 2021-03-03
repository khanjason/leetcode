# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotone(self,head):
        n=head
        while n.next:
            n=n.next
        end=n
        t=head
        while t.next:
            
            if t.next==end:
                break
            t=t.next
        
        end.next=head
        t.next=None
        return end
    def getlen(self,head):
        n=head
        tot=0
        while n:
            tot+=1
            n=n.next
        return tot
    
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head==None:
            return None
        l=self.getlen(head)
        
        for y in range(0,k%l):
            head=self.rotone(head)
        return head
        
