class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxx=0
        pali=''
        res = [s[i: j] for i in range(len(s)) 
          for j in range(i + 1, len(s) + 1)] 
        for i in res:
            if i == i[::-1]:
                if len(i)>maxx:
                    maxx=len(i)
                    pali=i
        return pali
  
