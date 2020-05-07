class Solution:
    
    def removedata(self,s):
        ind=0
        for t in s:
            if t=='(':
                break
            ind=ind+1
        return ind
    
    def getdata(self,path):
        s=path[::-1]
        d=''
        for i in s:
            if i=='(':
                break
            else:
                if i!=')':
                    d=d+i
        return d
            
    
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        newpaths=[]
        groups=[]
        uniq=[]
        for t in paths:
            newpaths.append(t.split(' '))
        
        
        for thing in newpaths:
            start=thing[0]
            thing[0]=start+'/'
        print(newpaths)
        for package in newpaths:
            for i in range(1,len(package)):
                d=(self.getdata(package[i]))
                if d not in uniq:
                    
                    uniq.append(d)
                    strr=package[0]+package[i]
                    cut=self.removedata(strr)
                    groups.append([strr[:cut]])
                else:
                    ind=uniq.index(d)
                    strr=package[0]+package[i]
                    cut=self.removedata(strr)
                    groups[ind].append(strr[:cut])
                    
        finalgroups=[]
        for g in groups:
            if len(g)>1:
                finalgroups.append(g)
        return finalgroups
                    
