class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        ans=(num **0.5)
        if ans == int(ans):
            return True
        return False
