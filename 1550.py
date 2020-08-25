class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        FirstOdd=False
        SecondOdd=False
        for i in arr:
            if i%2==1:
                if FirstOdd==False:
                    FirstOdd=True
                else:
                    if SecondOdd==True:
                        return True
                    else:
                        SecondOdd=True
            else:
                FirstOdd=False
                SecondOdd=False
        return False
