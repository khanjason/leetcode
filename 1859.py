class Solution:
    def sortSentence(self, s: str) -> str:
        li=s.split(" ")
        tot=len(li)
        arr=[]
        for i in range(0,tot):
            arr.append(0)
        for item in li:
            n=int(item[-1])-1
            arr[n]=item[:len(item)-1]
        ans=arr[0]
        for t in range(1,len(arr)):
            ans=ans+" "
            ans=ans+arr[t]
        return ans