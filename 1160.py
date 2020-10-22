class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        #word={alphabet:number of chars in word}
        worddicts=[]
        valid=[]
        chars=list(chars)
        alph=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        for w in words:
            worddict={}
            for a in alph:
                worddict[a]=w.count(a)
            worddicts.append(worddict)
        for d in range(0,len(worddicts)):
            validb=True
            for c in words[d]:
                if c not in chars:
                    validb=False
                elif worddicts[d][c]>chars.count(c):
                    validb=False
            if validb==True:
                valid.append(words[d])
        count=0
        for t in valid:
            for y in t:
                count=count+1
        return count
                
