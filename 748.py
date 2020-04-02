class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        parts=[]
        counts=[]
        good=""
        numbers="1234567890 "
        newwords=[]
        licensePlate=licensePlate.lower()
        for i in licensePlate:
            if i.lower() not in parts:
                if i not in numbers:
                    parts.append(i.lower())
                    counts.append(licensePlate.count(i.lower()))
        

        for word in words:
            adding=True
            for let in parts:
                if let not in word.lower():
                    adding=False
                    break
            if adding==True:
                newwords.append(word)
        
        
        for w in newwords:
            fine=True
            for t in w:
                if t in parts:
                    ind=parts.index(t)
                    if w.count(t)<counts[ind]:
                        fine=False
                        break
                
            if fine==True:
                if good=="": 
                    good=w
                elif len(w)<len(good):
                    good=w
        return(good)
        
