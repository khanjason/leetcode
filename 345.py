class Solution:
    def reverseVowels(self, s: str) -> str:
        if s==" ":
            return " "
        slist=[]
        vows=[]
        vowels=['a','e','i','o','u']
        for item in range(0,len(s)):
            if s[item].lower() in vowels:
                vows.append(s[item])
                slist.append('7365378')
            else:
                slist.append(s[item])
        for it in range(0,len(slist)):
            if slist[it]=='7365378':
                slist[it]=vows.pop()
        return(''.join(slist))
            
