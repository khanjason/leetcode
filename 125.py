class Solution:
    def isPalindrome(self, s: str) -> bool:
        stt=""
        if s==stt or s==" " or len(s)<2:
            return True
        alp='abcdefghijklmnopqrstuvwxyz0123456789'
        for i in s:
            if i.lower() in alp:
                stt=stt+i.lower()
        
        mid=int(len(stt)/2)
        
        if stt==" " or len(stt)<2:
            return True
 
        if len(stt) %2==1:
            first=(stt[:mid])
            second=(stt[mid+1:])
            rev=second[::-1]
            if rev==first:
                return True
        else:
            first=(stt[:mid])
            second=(stt[mid:])
            rev=second[::-1]
            if rev==first:
                return True
        return False
            
