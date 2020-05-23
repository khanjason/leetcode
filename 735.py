class Solution:
  
    
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        left=[]
        for a in asteroids:
            while left and a <0 <left[-1]:
                if left[-1]<-a:
                    left.pop()
                    continue
                elif left[-1]==-a:
                    left.pop()
                    
                break
            else:
                left.append(a)
                    
        return left
