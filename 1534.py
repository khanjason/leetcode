from itertools import combinations
class Solution(object):
    def countGoodTriplets(self, arr, a, b, c):
        """
        :type arr: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        res=[]
        oc= combinations(arr,3)
        for i in list(oc):
            
            if abs((i[0])-(i[1])) <=a:
                
                if abs(i[1]-i[2]) <=b:
                    if abs((i[0])-(i[2])) <=c:
                        res.append(i)
        return len(res)
                        
