class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in range(len(asteroids)):
            stack.append(asteroids[i])
            while len(stack)>1 and math.copysign(1,stack[-2])==1 and math.copysign(1,stack[-1])==-1:
                if abs(stack[-1])>abs(stack[-2]):
                    stack.pop()
                    stack.pop()
                    stack.append(asteroids[i])
                elif abs(stack[-1])==abs(stack[-2]):
                    stack.pop()
                    stack.pop()
                elif abs(stack[-1])<abs(stack[-2]):
                    stack.pop()
                
        return(stack)
            

        