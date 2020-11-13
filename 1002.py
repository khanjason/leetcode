class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        alp={}
        first=A[0]
        for t in first:
            if t not in alp.keys():
                alp[t]=1
            else:
                alp[t]+=1
        s=set(alp.keys())
        for word in A[1:]:
            for letter in s:
                if letter not in word:
                    #remove from dict
                    if letter in alp.keys():
                        del alp[letter]
                   
                else:
                    if letter in alp.keys():
                        if alp[letter]> word.count(letter):
                            alp[letter]=word.count(letter)
        
        ans=[]
        for k,v in alp.items():
            for n in range(v):
                ans.append(k)
        return ans
