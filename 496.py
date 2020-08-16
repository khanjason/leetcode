class Solution:
    def nextnum(self,n,li,ind):
        for item in range(ind,len(li)):
            if li[item] > n:
                return li[item]
        return -1
    
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        
        for n in nums1:
            index=nums2.index(n)
            ans.append(self.nextnum(n,nums2,index))
            
        return ans
