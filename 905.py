class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        s1=''
        s2=''
        outarray=[]
        for item in A:
            if item %2==0:
                s1=s1+str(item)
                s1=s1+'/'
            else:
                s2=s2+str(item)
                s2=s2+'/'
        s=s1+s2
        arr=s.split('/')
        arr=arr[:len(arr)-1]
        for i in arr:
            outarray.append(int(i))
        return outarray
