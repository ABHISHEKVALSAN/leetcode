class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        MAX_INT = 10**7
        MIN_INT = MAX_INT * -1

        if len(nums1)==0:
            n = len(nums2)
            if n%2==0:
                return (nums2[n//2] + nums2[(n//2)-1])/2.0
            else:
                return nums2[n//2]

        if len(nums2)==0:
            n = len(nums1)
            if n%2==0:
                return (nums1[n//2] + nums1[(n//2)-1])/2.0
            else:
                return nums1[n//2]

        n1 = len(nums1)
        n2 = len(nums2)

        if n1 > n2:
            nums1, nums2 = nums2, nums1
            n1, n2 = n2, n1

        if (n1 + n2)%2==0:
            mid1 = (n1+n2)//2
            mid2 = (n1+n2)//2 - 1
            if nums1[-1] <= nums2[0]:
                if n1-1 > mid2:
                    return (nums1[mid1] + nums1[mid2])/2.0
                elif n1-1 == mid2:
                    return (nums1[mid2] + nums2[0])/2.0
                elif n1-1 < mid2:
                    return (nums2[mid1 - n1] + nums2[mid2 - n1])/2.0
            elif nums2[-1] <= nums1[0]:
                if n2-1 > mid2:
                    return (nums2[mid2]+nums2[mid1])/2.0
                elif n2-1==mid2:
                    return (nums2[mid2]+nums1[0])/2.0
                elif n2-1 < mid2:
                    return (nums1[mid1- n2]+ nums1[mid2 - n2])/2.0
        else:
            mid = (n1 + n2)//2
            if nums1[-1] <= nums2[0]:
                if n1-1 >= mid:
                    return nums1[mid]
                elif n1-1 < mid:
                    return nums2[mid - n1]
            elif nums2[-1] <= nums1[0]:
                if n2-1 >= mid:
                    return nums2[mid]
                elif n2-1 < mid:
                    return nums1[mid-n2]
        
        if (n1+n2)%2==0:
            l = 0
            r = n1
            num = (n1+n2)//2
            while l<=r:
                mid = (l+r)//2
                l1 = nums1[mid-1] if mid-1 >=0 else MIN_INT
                r1 = nums1[mid] if mid < n1 else MAX_INT
                l2 = nums2[num-mid-1] if num-mid-1 >= 0 else MIN_INT
                r2 = nums2[num-mid] if num - mid < n2 else MAX_INT
                if l1 <= r2 and l2 <= r1:
                    return (max(l1,l2)+min(r1,r2))/2.0
                elif l1 > r2:
                    r = mid - 1
                elif l2 > r1:
                    l = mid + 1
        else:
            l = 0
            r = n1
            lnum = (n1 + n2 + 1)//2
            while l<=r:
                mid = (l+r)//2
                l1 = nums1[mid-1] if mid-1>=0 else MIN_INT
                r1 = nums1[mid] if mid < n1 else MAX_INT
                l2 = nums2[lnum-mid-1] if lnum-mid-1>=0 else MIN_INT
                r2 = nums2[lnum-mid] if lnum-mid < n2 else MAX_INT
                if l1 <= r2 and l2 <= r1:
                    return max(l1,l2)
                elif l2 > r1:
                    l = mid + 1
                elif l1 > r2:
                    r = mid - 1




