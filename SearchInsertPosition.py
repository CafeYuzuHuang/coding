class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 2021.03.12
        # 1st/3rd solution (3rd is minor rev. of 1st)
        # edge cases: note the order cannot be changed
        try:
            assert nums != []
            assert nums[0] < target
        except:
            return 0
        try: 
            assert nums[-1] >= target
        except:
            return len(nums)
        try:
            assert len(nums) != 2
        except:
            return 1 # squeezed
        
        # Bisection:
        m = 0
        n = len(nums) // 2
        while True:
            xx = m+n # 3rd approach
            yy = xx-1
            left = nums[yy] - target
            right = nums[xx] - target
            if left == 0:
                return yy
            elif left * right <= 0: # This statement deals with the insertion!
                return xx
            elif right > 0: # and left > 0
                n = len(nums[m:xx]) // 2 # close to the head
            elif right < 0: # and left < 0
                m += n
                n = len(nums[m:]) // 2 # close to the tail
                
        # 4th solution: standard binary search, time complexity O(logN)
        """
        # edge cases: note the order cannot be changed
        try:
            assert nums != []
            assert nums[0] < target
        except:
            return 0
        try: 
            assert nums[-1] >= target
        except:
            return len(nums)
        try:
            assert len(nums) != 2
        except:
            return 1 # squeezed
        
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
        # crossed, i.e. low > high
        return low # deal with the insertion
        """
        
        # 5th solution: standard binary search, time complexity O(logN)
        # no edge cases testing
        """
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
        # crossed, i.e. low > high
        return low # deal with the insertion
        """
        
        # 1st solution runtime 32 ms (84%), memory 14 MB (83%)
        # 3rd solution runtime 32 ms (84%), memory 14.1 MB (83%)
        # 4th solution runtime 36 ms (61%), memory 14 MB (83%)
        # 5th solution runtime 36 ms (61%), memory 14.2 MB
        
