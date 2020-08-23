class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type queryTime: int
        :rtype: int
        """
        count=0
        for i in range(0,len(startTime)):
            if queryTime >= startTime[i] and queryTime <= endTime[i]:
                count=count+1
        return count
