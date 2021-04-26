class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # 2021.04.26
        # target: O(1) space and O(n) time complexity
        # Note: all numbers are unique and only one missing number
        
        # 1st solution: model solution
        # sum = n*(n-1)/2
        """
        n = len(nums)
        return int(n*(n+1)/2) - int(sum(nums))
        """
        
        # 2nd solution: bit manipulation
        # see https://leetcode.com/problems/missing-number/solution/
        #
        # e.g.
        # nums = [0, 4, 1, 2], n = 4
        # missing number = 4 ^ (0 ^ 0) ^ (4 ^ 1) ^ (1 ^ 2) ^ (2 ^ 3)
        # = 4 ^ 4 ^ 0 ^ 0 ^ 1 ^ 1 ^ 2 ^ 2 ^ 3 = 0 ^ 0 ^ 0 ^ 0 ^ 3 = 3
        
        res = len(nums)
        for i, num in enumerate(nums):
            res ^= (i ^ num) # use XOR operator
        return res
        
        # 1st solution: 124 ms (86%), 15.4 MB (80%)
        # 2nd solution: 132 ms (54%), 15.5 MB (51%)
        
