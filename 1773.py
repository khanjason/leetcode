class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        types={}
        color={}
        name={}
        for l in range(0,len(items)):
            types[l]=items[l][0]
            color[l]=items[l][1]
            name[l]=items[l][2]
        count=0
        if ruleKey=="color":
            d=color
        elif ruleKey=="type":
            d=types
        else:
            d=name
        for k in d.keys():
            #print(d[k])
            if d[k]==ruleValue:
                
                count=count+1
        return count
