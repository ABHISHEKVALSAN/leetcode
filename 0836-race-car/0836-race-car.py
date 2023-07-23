from collections import deque
class Solution:
    def racecar(self, target: int) -> int:
        queue = deque()
        queue.append((0,0,1))
        visited = set()
        while queue:
            step, pos, speed = queue.popleft()
            if pos==target:
                return step
            if (pos,speed) not in visited:
                visited.add((pos,speed))
                queue.append((step+1,pos+speed,speed*2))
                if (pos+speed > target and speed>0) or \
                    (pos+speed<target and speed<0):
                    speed = -1 if speed > 0 else 1
                    queue.append((step+1,pos,speed))
        return 0

            
        return dp[target]


