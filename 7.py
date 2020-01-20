class Solution:
    def reverse(self, x: int) -> int:
        stri=str(x)
        li=[]
        end=""
        for ch in stri:
            if ch =='-':
                end="-"
            else:
                print(ch)
                li.append(ch)
        
        li2=li[::-1]
        print(li2)
        
        for thing in li2:
            end=end+thing
       
        lis=[]
        end2=end
        print("this is end2 " + end2)
        if '-' in end2:
            end2=end2[1:]
        while int(end2) >=1:
            e2=(int(end2)%2)
            print(int(end2)%2)
            lis.append(e2)
            end2=int(int(end2)/2)
            #print(end)
            
        lis=lis[::-1]
        print(lis)
        if len(lis)>=32:
            return(0)
        else:
        
            return(int(end))

        
