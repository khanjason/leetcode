class Solution:
    
    
    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) 
-> float:
        
        combi=[]
        for item in nums1:
            combi.append(item)
        for i in nums2:
            combi.append(i)
        
        n = len(combi) 
  
        # Traverse through all array elements 
        for i in range(n): 
            swapped = False
            # Last i elements are already in place 
            for j in range(0, n-i-1): 

                # traverse the array from 0 to n-i-1 
                # Swap if the element found is greater 
                # than the next element 
                if combi[j] > combi[j+1] : 
                    combi[j], combi[j+1] = combi[j+1], combi[j] 
                    swapped = True
            if swapped == False: 
                    break
        

        
        #s=(sum(combi))
        l=(len(combi))
      
        h=int(l/2)
        if l % 2==0:
            val1=combi[h]
            val2=combi[h-1]
            
            return ((val1+val2)/2)
      
        ans=float(combi[h])
        
        return ans
