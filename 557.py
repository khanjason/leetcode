class Solution:
    def reverseWords(self, s: str) -> str:
        li=[]
        w=''
        for i in s:
            if i == ' ':
                li.append(w[::-1])
                li.append(' ')
                w=''
            else:
                w=w+i
        li.append(w[::-1])
        return ''.join(li)
