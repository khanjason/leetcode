class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr=[first]
        #first xor unknown= encoded[0]
        #unknown = first xor encoded[0]
        for i in range(0,len(encoded)):
            arr.append(arr[i]^encoded[i])
        return(arr)
