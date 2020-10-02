import re
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        
        str = str.strip()
        L= re.findall('^[+-]?[0-9]+', str)

        try:
            num = int(L[0])
            if num < -2147483648:
                return -2147483648
            elif num > 2147483647:
                return 2147483647
            return num
        except:
            return 0
