class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        boolarr=[]
        for i in range(0,len(candies)):

            if candies[i]+extraCandies>=max(candies):
                    boolarr.append(True)
            else:
                boolarr.append(False)
        return boolarr
            
