class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 2021.04.01 
        # To search the max area in the x-y plane
        
        # 2nd solution: brute force, O(n^2) time complexity
        """
        n = len(height)
        if n <= 1: return 0
        elif n == 2: return min(height)
        
        amax = 0
        for i in range(n):
            for j in range(i, n):
                a1 = (j-i)*min(height[i],height[j])
                amax = max(amax, a1)
            for j in range(i):
                a2 = (i-j)*min(height[i],height[j])
                amax = max(amax, a2)
        return amax
        """
        
        # 3rd solution: two-pointer
        # Time complexity: O(n); space complexity: O(1)
        """
        n = len(height)
        if n <= 1: return 0
        elif n == 2: return min(height)
        
        i = 0
        j = n-1
        amax = 0
        while i < j:
            amax = max(amax, (j-i)*min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return amax
        """
        
        # 4th solution: optimized
        # Do not use min and max call function
        n = len(height)
        if n <= 1: return 0
        elif n == 2: return height[1] if height[1] < height[0] else height[0]
        
        i = 0
        j = n-1
        amax = 0
        atmp = 0
        while i < j:
            try:
                assert height[i] < height[j]
                atmp = height[i]*(j-i)
                i += 1
            except:
                atmp = height[j]*(j-i)
                j -= 1
            try:
                assert atmp < amax
            except:
                amax = atmp
        return amax
        
        # 2nd solution: time limit exceeded
        # 3rd solution: 720 ms (26%), 26.6 MB (28%)
        # 4th solution: 692 ms (31%), 26.4 MB (32%)
        
