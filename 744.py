class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        done=letters
        for i in range(1,26):
            val= chr((ord(target) - ord('a')+i) %26 + ord('a'))
            if val in done:
                return val
