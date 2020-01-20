# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1==None and l2==None:
            return None
        if l1==None and l2!=None:
            return l2
        if l1!=None and l2==None:
            return l1
        lm1=l1
        lm2=l2
        onelist=[]
        twolist=[]
        jointlist=[]
        finalist=[]
        testlist=[]
        nodeslist=[]
        onelist.append(lm1.val)
        while lm1.next!=None:
            #print(lm1.val)
            lm1=lm1.next
            onelist.append(lm1.val)
        twolist.append(lm2.val)
        while lm2.next!=None:
           # print(lm2.val)
            lm2=lm2.next
            twolist.append(lm2.val)
            
        
        for item in onelist:
            #print(item)
            jointlist.append(int(item))
        for thing in twolist:
            jointlist.append(int(thing))
        
        
        for thing in jointlist:
            finalist.append(int(thing))
        #print (finalist.sort())
      
        for item in onelist:
            testlist.append(item)
            testlist.sort()
        
        for item in twolist:
            testlist.append(item)
            testlist.sort()
        
            
       
       
        for item in range(0,len(testlist)):
            thi=ListNode(testlist[item])
            nodeslist.append(thi)
        for nod in range(0,len(nodeslist)):
            if nod != (len(nodeslist)-1):
                (nodeslist[nod]).next=nodeslist[nod+1]
            else:
                (nodeslist[nod]).next=None
       
        return nodeslist[0]
