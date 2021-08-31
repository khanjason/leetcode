class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        #ife even start with white
        #1 is black, 0 is white
        odds=[1,0,1,0,1,0,1,0]
        evens=[0,1,0,1,0,1,0,1]
        alp='abcdefgh'
        let=coordinates[0]
        num=int(coordinates[1])
        ind=alp.index(let)
        ans=0
        if num%2==0:
            ans=evens[ind]
        else:
            ans=odds[ind]
        return ans==0