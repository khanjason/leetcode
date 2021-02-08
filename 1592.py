class Solution:
    def reorderSpaces(self, text: str) -> str:
        countspace=text.count(' ')
        
        if countspace==0:
            return text
        wordl=text.split()
        wordcount=len(wordl)
        
        if wordcount==1:
            return wordl[0]+(' '*countspace)
        if countspace%(wordcount-1)==0:
            gap=int(countspace/(wordcount-1))
            gaps=' '*gap
            
            s=''
            for w in range(0,len(wordl)-1):
                s=s+wordl[w]+gaps
            s=s+wordl[-1]
            return s
        else:
            gap=int(countspace/(wordcount-1))
            r=countspace%(wordcount-1)
            rs=' '*r
            gaps=' '*gap
            s=''
            for w in range(0,len(wordl)-1):
                s=s+wordl[w]+gaps
            s=s+wordl[-1]+rs
            return s
