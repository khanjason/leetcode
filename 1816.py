class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        li=s.split(" ")
        return ' '.join(li[:k])