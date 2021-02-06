class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        nums=sorted(nums,reverse=True)
        d={}
        for i in nums:
            if i not in d.keys():
                d[i]=1
            else:
                d[i]+=1
        d=dict(sorted(d.items(), key=lambda item: item[1]))
        print(d)
        ans=[]
        for k,v in d.items():
            for i in range(0,v):
                ans.append(k)
                
        return ans
