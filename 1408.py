class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        sub=[]
        for w in range(0,len(words)):
            sli1=words[:w]
            for t in sli1:
                if words[w] in t:
                    sub.append(words[w])
                    break
            
            if words[w] not in sub:
            
                sli2=words[w+1:]
                for y in sli2:
                    if words[w] in y:
                        
                        sub.append(words[w])
                        break
        return sub
                    
                    
