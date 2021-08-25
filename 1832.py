class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        
        #remove all duplicates
        #check if equal length
        s=''
        for l in sentence:
            if l not in s:
                s=s+l
        return len(s)==26