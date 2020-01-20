class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        outputlist=[]
        for i in nums:
            left=target-i
            firstind= nums.index(int(i))
            #nums[nums.index(int(i))]= 'Na'
            if left in nums: #(nums.index(int(i))!= nums.index(int(left))) :
                if nums.count(i)>1 and i==left:
                    outputlist.append(nums.index(int(i)))
                    nums[nums.index(int(i))]= 'Na'
                    outputlist.append(nums.index(int(left)))
                    return outputlist
                elif i==left:
                    print(i)
                    print(left)
                    #nums[nums.index(int(i))]= 'Na'
                    
                else:
                    outputlist.append(nums.index(int(i)))
                    outputlist.append(nums.index(int(left)))
                
                    return outputlist
