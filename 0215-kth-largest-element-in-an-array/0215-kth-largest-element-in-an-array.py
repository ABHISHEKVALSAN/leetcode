import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums[:k]:
            heapq.heappush(heap, num)
        for num in nums[k:]:
            heapq.heappush(heap, num)
            heapq.heappop(heap)
        return heapq.heappop(heap)

