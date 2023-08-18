from collections import deque
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        vis = set([startGene])
        queue = deque([(startGene,0)])
        while queue:
            print(queue)
            curr_mut, step =  queue.popleft()
            if curr_mut==endGene:
                return step
            for i, valid_mut in enumerate(bank):
                if valid_mut in vis:
                    continue
                bit_diff = 0
                for j in range(8):
                    if curr_mut[j]!=valid_mut[j]:
                        bit_diff+=1
                        if bit_diff>1:
                            break
                if bit_diff==1:
                    queue.append((valid_mut,step+1))
                    vis.add(valid_mut)
        return -1
