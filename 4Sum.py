class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # 2021.04.13 
        # max length of nums = 200, O(n^2) or even O(n^3) might be acceptable
        
        # 5th solution: sorting + two-pointer + bisection, O(n^2logn)
        # extend to x sum: time complexity O(n^x-2*logn), looking for x > 2
        # ... failed
        # 8th solution: the pointer k should be rewinded when j moves
        # such results in O(n^3logn) time complexity
        """
        def bisect(nums, target, left, right):
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target: return mid
                elif nums[mid] > target: right = mid - 1
                else: left = mid + 1
            return left
        
        n = len(nums)
        if n < 4: return []
        nums = sorted(nums) # O(nlogn), less than the following O(n^2logn) nested loop
        res = []
        for i, ni in enumerate(nums[:-3]):
            j, k = i+1, n-1
            while j < k:
                nj, nk = nums[j], nums[k]
                n_ = target - ni - nj - nk
                _ = bisect(nums, n_, j+1, k-1)
                if _ < k and nums[_] == n_ :
                    tmp = sorted([ni, nj, n_, nk])
                    if not tmp in res: res.append(tmp)
                    k -= 1
                elif _ < k and nums[_] > n_: k -= 1
                else: j, k = j+1, n-1 
                # if _ >= k or nums[_] < n_, increase j and reset k
        return res
        """
        
        # 9th solution: use bisect module
        """
        n = len(nums)
        if n < 4: return []
        nums = sorted(nums) # O(nlogn), less than the following O(n^2logn) nested loop
        res = []
        for i, ni in enumerate(nums[:-3]):
            j, k = i+1, n-1
            while j < k:
                nj, nk = nums[j], nums[k]
                n_ = target - ni - nj - nk
                _ = bisect.bisect_left(nums, n_, j+1, k-1)
                if _ < k and nums[_] == n_ :
                    tmp = sorted([ni, nj, n_, nk])
                    if not tmp in res: res.append(tmp)
                    k -= 1
                elif _ < k and nums[_] > n_: k -= 1
                else: j, k = j+1, n-1 
                # if _ >= k or nums[_] < n_, increase j and reset k
        return res
        """
        
        # 6th solution: unsorted, hash set, time complexity O(n^3)
        # extend two sum solution to x sum, time complexity O(n^x-1)
        # this is the accepted solution #2, see
        # https://leetcode.com/problems/4sum/solution/
        
        def twoSum(nums, target):
            res = []
            s = set()
            for i in range(len(nums)):
                if len(res) == 0 or res[-1][1] != nums[i]:
                    if target - nums[i] in s:
                        res.append([target - nums[i], nums[i]])
                    s.add(nums[i])
            return res
        
        def kSum(nums, target, k):
            if len(nums) == 0 or nums[0]*k > target or target > nums[-1]*k:
                return []
            if k == 2: return twoSum(nums, target)
            res = []
            for i, ni in enumerate(nums):
                if i == 0 or nums[i-1] != nums[i]:
                    # kSum() return iterable object that can be used in enumerate loop
                    # and kSum() is called recursively
                    for _, c in enumerate(kSum(nums[i+1:], target-nums[i], k-1)):
                        res.append([nums[i]] + c)
            return res
        
        nums.sort()
        return kSum(nums, target, 4)
        
        
        # 7th solution: unsorted, hash set, time complexity O(n^3)
        # extend two sum solution to x sum, time complexity O(n^x-1)
        """
        def twoSum(nums, target):
            res = []
            d = {}
            for j, nj in enumerate(nums):
                if len(res) == 0 or res[-1][1] != nj:
                    try:
                        res.append([d[nj], nj])
                    except:
                        d[target-nj] = nj
            return res
        
        def kSum(nums, target, k):
            if len(nums) == 0 or nums[0]*k > target or target > nums[-1]*k:
                return []
            if k == 2: return twoSum(nums, target)
            res = []
            for i, ni in enumerate(nums):
                if i == 0 or nums[i-1] != nums[i]:
                    # kSum() return iterable object that can be used in enumerate loop
                    # and kSum() is called recursively
                    for _, c in enumerate(kSum(nums[i+1:], target-nums[i], k-1)):
                        res.append([nums[i]] + c)
            return res
        
        return kSum(sorted(nums), target, 4)
        """

        # 5th solution: failed to solve this problem using O(n^2logn) time complexity
        # 6th solution: 100 ms (81%) and 14.3 MB (80%)
        # 7th solution: 132 ms (74%) and 14.3 MB (57%)
        # 8th solution: 3260 ms (5%) and 14.4 MB (30%)
        # 9th solution: 1440 ms (15%) and 14.1 MB (99%)
