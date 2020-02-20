# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def convert(self,bina):

        
        tot=0
        count=0
        for i in range((len(bina)-1),-1,-1):
            if bina[count]=='1':
                
                tot=tot+(pow(2,i))#2**i)
            count+=1
        return(tot)
    def getDecimalValue(self, head: ListNode) -> int:
        s=''
        n=head
        while n!=None:
            s=s+str(n.val)
            n= n.next
        
        return(self.convert(s))
