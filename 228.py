class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if nums==[]:
            return []
        c=nums[0]
        ranges=[]
        t=[]
        for n in nums:
            if n!=c:
                ranges.append(t)
                t=[]
                c=n
                t.append(n)
                #new range
            else:
                t.append(n)
            c=c+1
        ranges.append(t)
        #print(ranges)
        ans=[]
        for r in ranges:
            s=''
            if len(r)!=1:
                s=s+str(r[0])
                s=s+'->'
                s=s+str(r[-1])
            else:
                s=str(r[0])
            ans.append(s)
        return ans
                
