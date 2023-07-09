from collections import deque
class Solution:

    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        if n==k:
            return 0
        arr = []
        for i in range(n-1):
            arr.append(weights[i]+weights[i+1])
        arr.sort()
        max_weight = sum(arr[n-k:])
        min_weight = sum(arr[:k-1])
        return max_weight - min_weight