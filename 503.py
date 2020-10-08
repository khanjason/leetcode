lass Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        r=[]
        for n in range(0,len(nums)):
            found=False
            if n==len(nums)-1:
                t=0
                if nums[t] > nums[n]:
                        r.append(nums[t])
                        found=True
                while nums[t]<=nums[n]:
                    
                    if t==n:
                        found=False
                        break
                    t=t+1
                    if nums[t] > nums[n]:
                        r.append(nums[t])
                        found=True
            
            else:
                for t in range(n,len(nums)):
                    if nums[t]>nums[n]:
                        r.append(nums[t])
                        found=True
                        break
                if found==False:
                    t=0
                    if nums[t] > nums[n]:
                            r.append(nums[t])
                            found=True
                    while nums[t]<=nums[n]:

                        if t==n:
                            found=False
                            break
                        t=t+1
                        if nums[t] > nums[n]:
                            r.append(nums[t])
                            found=True
            if found==False:
                r.append(-1)
        return r
