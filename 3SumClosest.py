class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # 2021.04.02
        
        # 4th solution: two-pointer, time complexity O(n^2)
        """
        nums, n = sorted(nums), len(nums)
        diff = 99999
        res = 99999
        if n == 3: return sum(nums)
        
        for i in range(n-2):
            # if i > 0 (True) and duplicate found
            if i and nums[i] == nums[i-1]: continue
            hi = n - 1
            lo = i + 1
            # all possible values are bounded by lo and hi, then start checking
            while lo < hi:
                sum3 = nums[i] + nums[lo] + nums[hi]
                if sum3 == target: return target
                elif abs(sum3 - target) < diff:
                    diff = abs(sum3 - target)
                    res = sum3
                    # Do not use the following while statements
                    # If hi - 1 = lo + 1 = hi XOR lo, it will be unexpected skipped.
                    # while lo < hi and nums[lo] == nums[lo+1]: lo += 1 
                    # while lo < hi and nums[hi] == nums[hi-1]: hi -= 1
                lo += (sum3 <= target) # if sum < 0, need larger lo
                hi -= (sum3 >= target) # if sum > 0, need smaller hi
        return res
        """
        
        # 5th solution: with binary search
        # Less efficient but more intuitive
        # Time complexity: O(n^2logn) (logn from BS)
        """
        nums, n = sorted(nums), len(nums)
        diff = 99999
        if n == 3: return sum(nums)
        
        for i in range(n-2):
            for j in range(i+1, n-1):
                comp = target - nums[i] - nums[j]
                hi = self.bisect(nums, comp, j+1, n-1)
                lo = hi - 1
                if hi < n and abs(comp - nums[hi]) < abs(diff): 
                    diff = comp - nums[hi]
                if lo > j and abs(comp - nums[lo]) < abs(diff):
                    diff = comp - nums[lo]
                if diff == 0: return target
        return target - diff
        
    def bisect(self, nums, target, low, high):
        # nums is sorted in ascent order
        # low >= 0, high <= len(nums)-1 are gueranteed
        left, right = low, high
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target: return mid
            elif nums[mid] > target: right = mid - 1
            elif nums[mid] < target: left = mid + 1
        # crossed, i.e. left > right
        return left
        """
        
        # 6th solution: rewrite of 4th
        
        nums, n, diff = sorted(nums), len(nums), 999999
        if n == 3: return sum(nums)
        for i in range(n-2):
            if i and nums[i] == nums[i-1]: continue
            hi, lo = n - 1, i + 1
            while lo < hi:
                sum3 = nums[i] + nums[lo] + nums[hi]
                if sum3 == target: return target
                elif abs(sum3 - target) < abs(diff): diff = sum3 - target
                lo += (sum3 <= target)
                hi -= (sum3 >= target)
        return diff + target
        
        
        # 4th solution: 104 ms (94%) and 14.4 MB (12%)
        # 5th solution: 548 ms (8%) and 14.5 MB (12%)
        # 6th solution: 108 ms (91%) and 14.44 MB (44%)
        
        # Since nums[i] ~ 1000, runtime for 5th is 1~10 times of 4th solution
        
