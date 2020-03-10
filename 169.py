class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj=int(len(nums)/2)
        counts=[]
        done=[]
        
        for n in nums:
            if n not in done:
                done.append(n)
                counts.append(0)
            ind=done.index(n)
            counts[ind]=counts[ind]+1
        maxcount=max(counts)
        indmaxcount=counts.index(maxcount)
        return done[indmaxcount]
