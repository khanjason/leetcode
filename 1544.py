class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=[]
        for i in range(0,len(s)):
            if stack==[]:
                stack.append(s[i])
            else:
                if (ord(stack[-1])-ord(s[i])==32) or (ord(stack[-1])-ord(s[i])==-32):
                    stack.pop()
                else:
                    stack.append(s[i])
        st=''
        if stack!=[]:
            for c in stack:
                st=st+c
        return st
     
