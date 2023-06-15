class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m==0:
            for i, e in enumerate(nums2):
                nums1[i] = e
        elif n!=0:
            i = 0
            j = 0
            while i < m and j < n:
                e = nums2[j]
                if nums1[i+j] > e:
                    temp = nums1[i+j]
                    nums1[i+j] = e
                    k = 0
                    while k < m-i:
                        temp1 = nums1[i+j+k+1]
                        nums1[i+j+k+1] = temp
                        temp = temp1
                        k+=1
                    j+=1
                else:
                    i+=1
                print(nums1,i,j)
            while j < n:
                nums1[i+j] = nums2[j]
                j+=1
