import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        i = 0
        n = len(nums)
        while i < n:
            if len(self.heap) < k:
                heapq.heappush(self.heap, nums[i])
            else:
                kl = heapq.heappop(self.heap)
                heapq.heappush(self.heap, max(kl,nums[i]))
            i+=1
            

    def add(self, val: int) -> int:
            if len(self.heap)< self.k:
                kl=val
            else:
                kl = heapq.heappop(self.heap)
            heapq.heappush(
                self.heap, 
                max(kl,val))
            ans = heapq.heappop(self.heap)
            heapq.heappush(self.heap,ans)
            return ans


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)