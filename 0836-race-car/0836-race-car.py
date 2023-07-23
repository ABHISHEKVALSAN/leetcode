from collections import deque
class Solution:
    def racecar(self, target: int) -> int:
        def solve(pos,speed,target):
            queue = deque()
            queue.append([0,1,0])
            visited = set()
            while queue:
                pos, speed, result = queue.popleft()
                if pos==target:
                    return result
                if (pos,speed) not in visited:
                    visited.add((pos,speed))
                    queue.append([pos+speed,speed*2,result+1])
                if pos+speed > target and speed > 0:
                    queue.append([pos,-1,result+1])
                if pos+speed < target and speed < 0:
                    queue.append([pos,1,result+1])
            return 0

        return solve(0,1,target)


