class Solution:
    def toGoatLatin(self, S: str) -> str:
        vowel=['a','e','i','o','u']
        wordli=[]
        c=''
        
        for thing in S:
            
            if thing==' ':
                
                wordli.append(c)
                
                c=''
            else:
                c=c+thing
        wordli.append(c)
        sentence=''
        counter=0
        for word in wordli:
            counter=counter+1
            if word[0].lower() in vowel:
                    sentence=sentence+(word+'ma'+('a'*((counter))))+' '
            else:
                    sentence=sentence+(word[1:]+word[0]+'ma'+('a'*(counter)))+' '
        sentence=sentence[:len(sentence)-1]
        return(sentence)
