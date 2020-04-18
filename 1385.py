class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        minn=d+1
        c=0
        minbool=False
        for i in range(0,len(arr1)):
            
            minbool=False
            for j in range(0,len(arr2)):
                if (abs(arr1[i]-arr2[j]) <minn):
                    
                    minbool=True
            if minbool==False:
                c=c+1
                    
                   
        return (c)
