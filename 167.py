class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in numbers:
            if i>target:
                break
            look=target-i
            if look in numbers:
                ind1=numbers.index(look)
                numbers[ind1]=" "
                return sorted([numbers.index(i)+1,ind1+1])
