class Solution:
    
    def getneighb(self,x,y,maxx,maxy):
        
        neighb=[[x,y]]
        if x==0 and y==0:
            
            neighb.append([x+1,y])
            
            neighb.append([x,y+1])
            neighb.append([x+1,y+1])
            
            
            
        elif x==0 and y==maxy:
            
            neighb.append([x+1,y])
            neighb.append([x,y-1])
            
            
            neighb.append([x+1,y-1])
            
        elif x==maxx and y==0:
            neighb.append([x-1,y])
            
            
            neighb.append([x,y+1])
            
            
            neighb.append([x-1,y+1])
        elif x==maxx and y==maxy:
            neighb.append([x-1,y])
            
            neighb.append([x,y-1])
            
            
            neighb.append([x-1,y-1])
            
            
        elif x==0:
            
            neighb.append([x+1,y])
            neighb.append([x,y-1])
            neighb.append([x,y+1])
            neighb.append([x+1,y+1])
            
            neighb.append([x+1,y-1])
            
        elif x==maxx:
            neighb.append([x-1,y])
            
            neighb.append([x,y-1])
            neighb.append([x,y+1])
            
            neighb.append([x-1,y-1])
            
            neighb.append([x-1,y+1])
        elif y==0:
            neighb.append([x-1,y])
            neighb.append([x+1,y])
            
            neighb.append([x,y+1])
            neighb.append([x+1,y+1])
            
            
            neighb.append([x-1,y+1])
        elif y==maxy:
            neighb.append([x-1,y])
            neighb.append([x+1,y])
            neighb.append([x,y-1])
            
            
            neighb.append([x-1,y-1])
            neighb.append([x+1,y-1])
            
        else:
            neighb.append([x-1,y])
            neighb.append([x+1,y])
            neighb.append([x,y-1])
            neighb.append([x,y+1])
            neighb.append([x+1,y+1])
            neighb.append([x-1,y-1])
            neighb.append([x+1,y-1])
            neighb.append([x-1,y+1])
        return neighb
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        maxx=len(M)-1
        print(maxx)
        
        maxy=len(M[0])-1
        print(maxy)
        if maxx==0 and maxy==0:
            return M
        elif maxx==0:
            a=[]
            t=[]
            for i in range(0,maxy+1):
                if i==0:
                    tot=M[0][i]+M[0][i+1]
                    av=int(tot/2)
                elif i==maxy:
                    tot=M[0][i]+M[0][i-1]
                    av=int(tot/2)
                else:
                    tot=M[0][i]+M[0][i-1]+M[0][i+1]
                    av=int(tot/3)
                t.append(av)
            a.append(t)
            return a
        elif maxy==0:
            ans=[]
            for i in range(0,maxx+1):
                if i==0:
                    t=[]
                    tot=M[i][0]+M[i+1][0]
                    av=int(tot/2)
                    t.append(av)
                    ans.append(t)
                elif i==maxx:
                    t=[]
                    tot=M[i][0]+M[i-1][0]
                    av=int(tot/2)
                    t.append(av)
                    ans.append(t)
                else:
                    t=[]
                    tot=M[i][0]+M[i+1][0]+M[i-1][0]
                    av=int(tot/3)
                    t.append(av)
                    ans.append(t)
            return ans
        smooth=[]
        for x in range(0,maxx+1):
            tmp=[]
            for y in range(0,maxy+1):
                neighbours=self.getneighb(x,y,maxx,maxy)
                tot=0
                number=len(neighbours)
                for n in neighbours:
                    tx=n[0]
                    ty=n[1]
                    print(n)
                    tot=tot+M[tx][ty]
                
                tmp.append(int(tot/number))
            smooth.append(tmp)
        
        return smooth
                
