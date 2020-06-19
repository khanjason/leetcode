import random
import numpy as np
class Solution:

    def __init__(self, nums: List[int]):
        self.li=nums
        self.copy=nums
    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.copy
        
        

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        array = self.li
        x = np.random.permutation(len(self.li))
        y = []
        for i in range(len(self.li)):
            y.append(array[x[i]])
        return y

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
