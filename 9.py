class Solution:
    def isPalindrome(self, x: int) -> bool:
        li=[]
        stri=str(x)
        mid=int(len(stri)/2)
        if len(stri)%2==1:
            cat=(stri[:mid])
            cat2=(stri[mid+1:])
        else:
            cat=stri[:mid]
            cat2=stri[mid:]
        cat2=cat2[::-1]
        print(cat)
        print(cat2)
        if (cat==cat2):
            return True
        else:
            return False
