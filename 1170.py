class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        answer=[]
        for q in queries:
            tot=0
            for w in words:
                if (q.count(min(q)))<(w.count(min(w))):
                    tot=tot+1
            answer.append(tot)
        return(answer)
