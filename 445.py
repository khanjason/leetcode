# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1=''
        root1=l1
        n=root1
        while n:
            s1=s1+str(n.val)
            n=n.next
        n=l2
        s2=''
        while n:
            s2=s2+str(n.val)
            n=n.next
        summ= str((int(s1))+(int(s2)))
        slist=[]
        for c in summ:
            slist.append(c)
        #print(slist)
        nodelist=[]
        for i in range(0,len(slist)):
            n=ListNode(int(slist[i]))
            nodelist.append(n)
        for node in range(0,len(nodelist)-1):
            
            nodelist[node].next=nodelist[node+1]
        return nodelist[0]
            
