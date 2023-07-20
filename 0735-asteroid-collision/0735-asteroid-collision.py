class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        i = 0
        n = len(asteroids)
        stack = []
        while i<n:
            if len(stack)==0 or stack[-1]<0:
                stack.append(asteroids[i])
            else:
                if asteroids[i]>0:
                    stack.append(asteroids[i])
                else:
                    while len(stack)>0 and \
                          stack[-1]>0 and \
                          stack[-1] < -asteroids[i]:
                        stack.pop()
                    if len(stack)==0 or stack[-1] < 0:
                        stack.append(asteroids[i])
                    if len(stack)>0 and stack[-1]==-asteroids[i]:
                        stack.pop()
            i+=1
        return stack


        return asteroids