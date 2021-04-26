# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 2021.04.26
        
        # 1st solution: using bisect search, like what git offers 
        # time: O(logn), space: O(1)
        
        l, r = 1, n
        while l <= r:
            m = (l+r)//2
            m_ = isBadVersion(m)
            if m_: r = m-1
            else: l = m+1
        return l
        
        
        # 3rd solution: scanning
        # time: O(n), space: O(1)
        """
        i = n
        while i > 0:
            if not isBadVersion(i): return i+1
            i -= 1
        return 1
        """
        
        
        # 1st solution: 32 ms (44%), 14.3 MB (9%)
        # 3rd solution: time limit exceeded
        
        
