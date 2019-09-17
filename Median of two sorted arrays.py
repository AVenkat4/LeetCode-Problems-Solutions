class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        
        if m < n:
            return self.findMedianSortedArrays(nums2, nums1)
        
        lo, hi = 0, 2*n
        while lo <= hi:
            mid2 = (hi + lo)/2
            mid1 = m + n - mid2
            
            L1 = -float('inf') if mid1 == 0 else nums1[(mid1 - 1)/2]
            L2 = -float('inf') if mid2 == 0 else nums2[(mid2 - 1)/2]
            R1 = float('inf') if mid1 == m * 2 else nums1[mid1/2]
            R2 = float('inf') if mid2 == n * 2 else nums2[mid2/2]
            
            if L1 > R2:
                lo = mid2 + 1
            elif L2 > R1:
                hi = mid2 - 1
            else:
                return (max(L1, L2) + min(R1, R2))/2.0
        
        return -1