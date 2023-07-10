class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = []
        i = 0
        n = len(gas)
        while i < n:
            diff.append(gas[i]-cost[i])
            i+=1
        if sum(diff)<0:
            return -1
        i = 0
        ind = 0
        curr_sum = 0
        while i < n:
            curr_sum+=diff[i]
            if curr_sum < 0:
                curr_sum = 0
                ind = i+1
            i+=1
        return ind