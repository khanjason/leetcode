class Solution:
    
    def openit(self,rooms,stack,seen):
        n=stack.pop()
        for key in rooms[n]:
            if seen[key]==False:
                seen[key]=True
                stack.append(key)
                
        return stack
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        seen={}
        for i in range(len(rooms)):
            seen[i]=False
        seen[0]=True
        stack=[0]
        while stack:
            stack=self.openit(rooms,stack,seen)
            
        for k,v in seen.items():
            if v==False:
                return v
        return True
