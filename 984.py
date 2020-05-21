class Solution:
    def strWithout3a3b(self, A: int, B: int) -> str:
        #alternate
        s=''
        curr = 'a' if A>B else 'b'
        while A>0 or B>0:
            if curr == 'a':
                if A>B and A>1:
                    s =s+ "aa"
                    A -= 2
                else: 
                    s=s+ "a"
                    A -= 1
                curr = "b"
            else:
                if B>A and B>1:
                    s =s+ "bb"
                    B -= 2
                else: 
                    s=s+ "b"
                    B -= 1
                curr = "a"
                
        return s
