class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # 2021.03.16
        # 3rd solution: naive, time complexity O(N), N = m+n
        if n == 0:
            return None
        if m == 0:
            nums1[:] = nums2[:] # <--- for case nums1 = [0], m = 0, nums2 = [1], n = 1
            return None
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]: # compare their maximum values
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]
        return None
    
        # 20 ms (91%), 13.5 MB (46%)
    
    
