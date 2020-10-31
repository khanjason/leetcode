class Solution:
    def simplifyPath(self, path: str) -> str:
        curr=0
        stack=[]
        for item in path.split('/'):
            if item=='..' :
                if stack!=[]:
                    stack.pop()
            elif item=='.' or item=='':
                pass
            else:
                stack.append(item)
        print(stack)
        ans=''
        if stack==[]:
            return '/'
        for item in stack:
            ans=ans+'/'
            ans=ans+item
        return ans
        
