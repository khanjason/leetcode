class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        ttot=0
        for item in t:
            ttot=ttot+ord(item)
        #print(ttot)
        stot=0
        for thing in s:
            stot=stot+ord(thing)
        #print(stot)
        p=ttot-stot
        return (chr(p))
