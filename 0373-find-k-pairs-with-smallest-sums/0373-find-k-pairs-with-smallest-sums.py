from heapq import heappush as hpush, heappop as hpop,heappushpop as hpp
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        result = []
        n1 = len(nums1)
        n2 = len(nums2)
        visited = set()
        heap = [(nums1[0]+nums2[0],(0,0))]
        visited.add((0,0))
        itr = 0
        while itr < min(k,n1*n2):
            s, (i,j) = hpop(heap)
            result.append([nums1[i],nums2[j]])
            if i+1 < n1 and (i+1, j) not in visited:
                hpush(heap,(nums1[i+1]+nums2[j],(i+1,j)))
                visited.add((i+1,j))
            if j+1 < n2 and (i,j+1) not in visited:
                hpush(heap,(nums1[i]+nums2[j+1],(i,j+1)))
                visited.add((i,j+1))
            itr+=1
        return result