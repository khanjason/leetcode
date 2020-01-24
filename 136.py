class Solution:
    
    def delvalues(self,v,li):
        while v in li : 
            li.remove(v)
        return li
    def singleNumber(self, nums: List[int]) -> int:
        done=[]
        for i in nums:
            if i not in done:
                done.append(i)
            else:
                done.remove(i)
        return(done[0])
