class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a=''
        ans=[]
        for i in digits:
            a=a+str(i)
        s=int(a)+1
        st=str(s)
        for t in st:
            ans.append(int(t))
        return ans
