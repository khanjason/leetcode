class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        favset=[]
        inds=[]
        for f in favoriteCompanies:
            favset.append(set(f))
        for i in range(0,len(favset)):
            for t in range(0,len(favset)):
                if t==(len(favset)-1):
                    if (favset[i].issubset(favset[t]))==False or i==t:
                        
                        inds.append(i)
                elif favset[i].issubset(favset[t]) and i!=t:
                    
                    break
        return inds
                
