class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        ans=[]
        n=0
        for i in range(0,num_people):
            ans.append(0)
        while candies>0:
            for t in range(0,len(ans)):
                if candies>=(n+t+1):
                    ans[t]+=(n+t+1)
                    candies-=(n+t+1)
                else:
                    ans[t]+=(candies)
                    candies=0
                
                if t==len(ans)-1:
                    n=n+(len(ans))
        return ans
