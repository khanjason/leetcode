
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
            scores=[0]
            
            for i in range(0,len(arr)):
                scores.append(arr[i]^scores[i])
            total=0
            for i in range(1,len(arr)):
                for k in range(i+1,len(arr)+1):
                    if scores[i-1]==scores[k]:
                        total=total+(k-i)
       
            return total
