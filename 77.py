from itertools import combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        li=[]
        nums=[]
        for i in range(1,n+1):
            nums.append(i)
        c=combinations(nums,k)
        for p in list(c):
            li.append(list(p))
        return(li)
