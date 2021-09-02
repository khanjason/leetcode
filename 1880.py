class Solution:
    def getst(self,word):
        al='abcdefghijklmnopqrstuvwxyz'
        tot=''
        for i in word:
            ind=al.index(i)
            tot=tot+str(ind)
        return int(tot)
    
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        target=int(self.getst(targetWord))
        
        if (int(self.getst(firstWord)) +int(self.getst(secondWord))==target):
            return True
        return False