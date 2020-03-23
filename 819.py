class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        plist=[]
        abc=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y'
,'z']
        counts=[]
        for item in paragraph.split(" "):
            c=-1
            for let in item:
                c=c+1
                if let.lower() not in abc:
                    item=item[:c]
                    break
            
            plist.append(item.lower())
           
                
            
        for word in range(0,len(plist)):
            if (plist[word]).lower() in banned:
                plist[word]=" "
        for i in plist:
            if i is not " ":
                counts.append(plist.count(i))
            else:
                counts.append(0)
        m=max(counts)
        ind=counts.index(m)
        
        return(plist[ind])
