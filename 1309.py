class Solution:
    
    def freqAlphabets(self, s: str) -> str:
        d={'1':'a','2':'b','3':'c','4':'d','5':'e','6':'f','7':'g','8':'h','9':'i','10#':'j','11#':'k','12#':'l','13#':'m','14#':'n','15#':'o','16#':'p','17#':'q','18#':'r','19#':'s','20#':'t','21#':'u','22#':'v','23#':'w','24#':'x','25#':'y','26#':'z'}
        st=''
        li=[]
        oli=[]
        for i in s:
            if i=='#':
                st=st+i
                
                li.append(st)
                st=''
            else:
                st=st+i
        li.append(st)
        for thing in li:
            
            
            if len(thing)==2:
                pt1=thing[0]
                pt2=thing[1]
                oli.append(pt1)
                oli.append(pt2)
            elif len(thing)==3 or len(thing)==1:
                oli.append(thing)
            else:
                thi2=thing[:thing.find('#')-2]
                for it in thi2:
                    oli.append(it)
                thi=thing[thing.find('#')-2:thing.find('#')+1]
                
                oli.append(thi)

        print(li)
        print(oli)
        for k in oli:
            if k=='':
                oli.remove(k)
        
        output=''
        for item in oli:
            output=output+str(d[item])
        return output
