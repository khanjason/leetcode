class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morsea=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        translated=[]
        for word in words:
            s=''
            for let in word:
                ind1=alphabet.index(let)
                s=s+morsea[ind1]
            if s not in translated:
                translated.append(s)
        return len(translated)
