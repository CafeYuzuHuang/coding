class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 2021.03.16
        # 1st solution: induction & recursion (brute force)
        # n = 1  2  3  4  5  6 ...
        # x = 1  2  3  5  8  13 ...
        #          # of two-steps # of ways 
        # For n = 4: (2, 1, 0) = (1, 3, 1) = 5
        # For n = 5: (3, 2, 1, 0) = (0, 3, 4, 1) = 8
        # For n = 6: (3, 2, 1, 0) = (1, 6, 5, 1) = 13
        # For each n, no. of ways is that of n-2 plus that of n-1
        # meaning climb two steps from position n-2 and one step from n-1
        """
        if n <= 2:
            return n
        else:
            return self.climbStairs(n-2) + self.climbStairs(n-1)
        """
        
        # 2nd solution: The 1st solution cause time limit exception
        # Here we use another methods (Fibonacci number)
        """
        if n <= 2:
            return n
        a = 1
        b = 2
        for i in range(3, n+1):
            x = a + b
            a = b
            b = x
        return x
        """
        
        # 3rd solution: use dynamic programming
        if n <= 2:
            return n
        A = [0]*n
        A[0] = 1
        A[1] = 2
        for i in range(2, n):
            A[i] = A[i-1] + A[i-2]
        return A[-1]
        
        # 2nd solution: 16 ms (77%) and 13.4 MB (41%)
        # 3rd solution: 20 ms (46%) and 13.3 MB (91%)
        
        # Note:
        # Time complexity and space complexity:
        # Recursion: O(2^n), O(1) ... 1st solution
        # Iteration: O(N), O(1) ... 2nd solutions
        # Iteration: O(N), O(N) ... 3rd solutions
        # 1st is identified as brute force approach, 2nd is Fibonacci series, 3rd is dynamic programming!
