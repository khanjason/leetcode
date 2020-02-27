class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uni=[]
        for em in emails:
            s=''
            for t in em:
                
                if ord(t)==64:
                        break
                    
                elif t=='.':
                            pass
                elif t=='+':
                            break

                else:
                            s=s+t
            ind=em.find('@')
            s=s+em[ind:]
            if s not in uni:
                uni.append(s)
        return len(uni)
