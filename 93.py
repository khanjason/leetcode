from itertools import combinations
class Solution:
    def isvalid(self,s):
        l=s.split('.')
        for i in l:
            if len(i)!=len(str(int(i))):
                return False
            
            elif int(i) not in range(0,256):
                return False
        return True
    
    
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s)>12:
            return []
        places=[]
        indices=[]
        c=-1
        for i in range(len(s)):
            
            places.append(s[i])
            c=c+1
            if i!=len(s)-1:
                places.append('-')
                c=c+1
                indices.append(c)
        
        #print(places)
        #print(indices)
        copy=[]
        for y in places:
            copy.append(y)
        t=combinations(indices,3)
        ips=[]
        for tu in list(t):
            copy[tu[0]]='.'
            copy[tu[1]]='.'
            copy[tu[2]]='.'
            
            for thing in range(len(copy)):
                if copy[thing]=='-':
                    copy[thing]=''
            ips.append(''.join(copy))
            copy=[]
            for y in places:
                copy.append(y)
        #print(ips)
        fin=[]
        for ip in ips:
            if self.isvalid(ip):
                fin.append(ip)
        return fin
            
