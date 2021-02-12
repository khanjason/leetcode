class Solution:
    
    def rotate(self,lis,n):
        new=[]
        for t in range(0,len(lis)):
            new.append(0)
        for y in range(0,len(lis)):
            new[y]=lis[(y+n)%len(lis)]
        return new
    
    def check(self, nums: List[int]) -> bool:
        s=sorted(nums)
        for i in range(0,len(nums)):
            new=self.rotate(s,i)
            
            if new==nums:
                return True
        return False
