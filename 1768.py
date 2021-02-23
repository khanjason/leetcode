class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s=''
        m=min(len(word1),len(word2))
        for i in range(0,m):
            s=s+word1[i]
            s=s+word2[i]
        if len(word1)==len(word2):
            return s
        maxx=max(len(word1),len(word2))
        if len(word1)==maxx:
            stub=word1[m:]
        else:
            stub=word2[m:]
        s=s+stub
        return s
