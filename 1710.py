class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        #trucksize is max number of boxes
        boxTypes=sorted(boxTypes, key = lambda x: int(x[1]), reverse=True)
        print(boxTypes)
        units=0
        for boxes in boxTypes:
            if truckSize==0:
                break
            for i in range(boxes[0]):
                if truckSize==0:
                    break
                truckSize-=1
                units+=boxes[1]
            
        return units
