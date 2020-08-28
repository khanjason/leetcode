class Solution(object):
    
    def sub_lists(self,list1): 
  
        
        sublist = [] 

        
        for i in range(len(list1)): 

            summ=0
            for j in list1[i:]: 

                summ=summ+j
                
                sublist.append(summ) 


        return sublist 
  
    
    def rangeSum(self, nums, n, left, right):
        """
        :type nums: List[int]
        :type n: int
        :type left: int
        :type right: int
        :rtype: int
        """
        subsums=[]
        sublist=self.sub_lists(nums)
        #for s in sublist:
          #  if s!=[]:
           #     subsums.append(sum(s))
        li=sorted(sublist)
        
        return (sum(li[left-1:right]))% ((10**9)+7)
