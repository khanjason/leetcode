class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1='qwertyuiop'
        row2='asdfghjkl'
        row3='zxcvbnm'
        a=[]
        dis=[]
        row=0
        for word in words:
            row=0
            for let in word:
                if row!=0:
                    
                    if let.lower() not in row:
                            dis.append(word)
                            break
                if let.lower() in row1:
                    row=row1
                if let.lower() in row2:
                    row=row2
                if let.lower() in row3:
                    row=row3
        for item in dis:
            if item in words:
                words.remove(item)
        return(words)
