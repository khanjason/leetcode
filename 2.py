# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        first=[]
        n=l1
        first.append(n.val)
        while n.next:
            
            n=n.next
            first.append(n.val)
        first=first[::-1]
        second=[]
        n2=l2
        second.append(n2.val)
        while n2.next:
            
            n2=n2.next
            second.append(n2.val)
        second=second[::-1]
        print(first,second)
        f=''
        s=''
        for item in first:
            f=f+str(item)
        for t in second:
            s=s+str(t)
        value=str(int(f)+int(s))
        value=value[::-1]

        ans=ListNode()
        c=0
        a=ans

        while c<len(value):
            
            print(value[c])
            a.val=value[c]
            
            if c<len(value)-1:
                b=ListNode()
                a.next=b
                a=b
            c=c+1
        return ans
