class Solution:
    def defangIPaddr(self, address: str) -> str:
        li=[]
        s=''
        for t in address:
            if t=='.':
                li.append(s)
                li.append('[.]')
                s=''
            else:
                s=s+t
        li.append(s)
        print(li)
        stre=''
        for thing in li:
            stre=stre+thing
        return stre
