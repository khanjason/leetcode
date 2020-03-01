class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l=len(s)-1
        c=-1
        m=int(len(s)/2)
        for i in range(l,0,-1):
            c=c+1
            if c==m:
                break
            
            s[i], s[c]=s[c], s[i]
        print(s)
