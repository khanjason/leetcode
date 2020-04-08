from itertools import combinations
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        #[i,j,k]
        teams=0
        c=combinations(rating,3)
        for i in c:
            t=(tuple(i))
            if t[0]<0:
                break
            if (t[0]<t[1]) and (t[1]<t[2]):
                teams=teams+1
            elif (t[0]>t[1]) and (t[1]>t[2]):
                teams=teams+1
        return (teams)
        
