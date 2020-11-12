class Solution:
    def maxArea(self, height: List[int]) -> int:
        #two pointers for x and y mutiplied
        tot=0
        length=len(height)-1
        i=0 
        j=length 
        c=0
        while i<j:
           
                    
            h=min(height[i],height[j])
            l=j-i
            tmp=h*l
            tot=max(tmp,tot)
            if height[i]<height[j]:
                i=i+1
            else:
                j=j-1
               
        return(tot)
