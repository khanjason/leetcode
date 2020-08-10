class Solution:
    def checkpref(self,stub,word):
        for t in range(0,len(word)):
            if stub==word[:t+1]:
                return True
        return False
    
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sent=sentence.split(' ')
        for i in range(0,len(sent)):
            if self.checkpref(searchWord,sent[i]):
                return i+1
        return -1
