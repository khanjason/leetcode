class Solution:
    
    def makesuggestion(self,products,letters):
        prefs=[]
        for p in products:
            if p.startswith(letters):
                prefs.append(p)
        r=sorted(prefs)
        return r[:3]
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        #at most 3
        #output a list for each letter
        ans=[]
        s=''
        for l in searchWord:
            s=s+l
            
            ans.append(self.makesuggestion(products,s))
        return ans
