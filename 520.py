class Solution:
    
    def checkalllower(self,word):
        for i in word:
            if i.lower()!=i:
                return False
        return True
    def checkallcap(self,word):
        for i in word:
            if i.upper()!=i:
                return False
        return True
    def detectCapitalUse(self, word: str) -> bool:
        
        if len(word)<2:
            return True
        
        
        firstlet=word[0]
        firstchoice=None
        if firstlet.lower()==firstlet:
            firstchoice=1
        else:
            firstchoice=2
        
        if firstchoice==1:
            return self.checkalllower(word)
        elif firstchoice==2:
            secondlet=word[1]
            secondchoice=None
            if secondlet.lower()==secondlet:
                return self.checkalllower(word[1:])
            else:
                return self.checkallcap(word)
        else:
            return 0
        
