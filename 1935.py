class Solution:
    def getok(self,word,brokenlet):
        for t in word:
            if t in brokenlet:
                return False
        return True
    
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        te=text.split(" ")
        tot=0
        for item in te:
            if self.getok(item,brokenLetters):
                tot=tot+1
            
        return tot