class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 2021.04.29
        # e.g. [1, 2, 3, 3] -> [1, 3, 2, 3]
        # e.g. [1, 4, 3, 3] -> [3, 1, 3, 4]
        
        # 1st solution: iterative, single-pass
        # time complexity: O(n)
        # space complexity: O(1)
        # see https://leetcode.com/problems/next-permutation/solution/
        
        n = len(nums)
        if n == 1: return None
        if n == 2: 
            nums[0], nums[1] = nums[1], nums[0]
            return None
        i, j = n - 2, n - 1
        # search from right, move to left if descending 
        while i >= 0 and nums[i] >= nums[i+1]: i -= 1
        if i >= 0:
            # search from right, move to left if not larger than nums[i]
            while j >= 0 and nums[j] <= nums[i]: j -= 1
            nums[i], nums[j] = nums[j], nums[i] # swap the two element
        
        # Examine if lexicographically next greater permutation 
        # reverse order to ascent for elements right to i
        ii, jj = i+1, n-1
        while ii < jj:
            nums[ii], nums[jj] = nums[jj], nums[ii]
            ii += 1
            jj -= 1
        
        # 1st solution: 36 ms (91%), 14.4 MB (21%)
        
