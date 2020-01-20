class Solution:
    def convert(self, s: str, numRows: int) -> str:
        collection=[]
        for i in range(0,numRows):
            collection.append([])
        if numRows==1:
            return s
        count=0
        desc=False
        for thing in range(0,len(s)):
            #print(count)
            if count==(len(collection)-1):
                
                desc=True
            if desc==True and count==0:
                desc=False
            collection[count].append(s[thing])
            if desc==False:
                count=count+1
            if desc==True:
                count=count-1
        #print(collection)
        finalstring=""
        for item in collection:
            for thing in item:
                finalstring=finalstring+thing
        return(finalstring)
