class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.strip()
        wrev=s.split(" ")
        for i in range(0,len(wrev)):
            wrev[i]=wrev[i].strip()
            
        
        s=''
        for word in wrev[::-1]:
            if word!='':
                s=s+word
                s=s+' '
        return s[:len(s)-1]
