class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 2021.04.02
        # 2nd solution: brute force method, 
        # O(n^3) time complexity
        # O(n) space complexity
        """
        n = len(nums)
        if n < 3: return []
        res = []
        for i in range(n):
            for j in range(i+1, n):
                k = j+1
                while k < n:
                    ni, nj, nk = nums[i], nums[j], nums[k]
                    tmp = []
                    if ni + nj + nk == 0:
                        tmp = sorted([ni, nj, nk])
                        if not tmp in res: res.append(tmp)
                    k += 1 # to guerantee i < j < k
        return res
        """
        
        # 3rd solution: hash table, O(n^2) time complexity, O(n) space complexity
        # r.f. problem 1: target -> ni, num -> nj, i -> j
        """
        n = len(nums)
        if n < 3: return []
        res = []
        
        for i, ni in enumerate(nums):
            nums_dict = {}
            for j in range(i+1, n): # guerantee j > i
                nj = nums[j]
                nk = -ni - nj
                try:
                    if j != nums_dict[nj]: # past j = k, past nj = nk
                        ijk = sorted([ni, nj, nk])
                        if not ijk in res: res.append(ijk)
                except:
                    pass
                nums_dict[nk] = j
        return res
        """
        
        # 4th solution: sorting, time complexity O(nlogn + n^2), space O(n)
        """
        n = len(nums)
        if n < 3: return []
        snums = sorted(nums) # ascent
        if snums[0] > 0 or snums[-1] < 0: return []
        res = []
        
        for i, ni in enumerate(snums):
            if ni > 0: break # nj and nk > 0
            nums_dict = {}
            for j in range(n-1, i, -1): # guerantee j > i
                nj = snums[j]
                nk = -ni - nj
                if nj < 0 and nk < 0: break # ni < 0
                try:
                    if j != nums_dict[nj]: # past j = k, past nj = nk
                        ijk = sorted([ni, nj, nk])
                        if not ijk in res: res.append(ijk)
                except:
                    pass
                nums_dict[nk] = j
        return res
        """
        
        # 5th solution:
        """
        n = len(nums)
        if n < 3: return []
        snums = sorted(nums) # ascent
        if snums[0] > 0 or snums[-1] < 0: return []
        res = []
        
        for i, ni in enumerate(snums):
            if ni > 0: break # nj and nk > 0
            nums_dict = {}
            for j in range(n-1, i, -1): # guerantee j > i
                nj = snums[j]
                nk = -ni - nj
                if nj < 0 and nk < 0: break # ni < 0
                if nj in nums_dict and j != nums_dict[nj]:
                    ijk = sorted([ni, nj, nk])
                    if not ijk in res: res.append(ijk)
                nums_dict[nk] = j
        return res
        """
        
        # 6th solution: further optimized
        """
        n = len(nums)
        if n < 3: return []
        snums = sorted(nums) # ascent
        if snums[0] > 0 or snums[-1] < 0: return []
        res = []
        
        for i, ni in enumerate(snums):
            if ni > 0: break # nj and nk > 0
            elif i > 0 and ni == snums[i-1]: continue # duplicated
            nums_dict = {}
            for j in range(n-1, i, -1): # guerantee j > i
                nj = snums[j]
                nk = -ni - nj
                if nj < 0 and nk < 0: break # ni < 0
                if nj in nums_dict and j != nums_dict[nj]:
                    # gueranteed: nk >= nj >= ni since snums is sorted
                    if not [ni, nj, nk] in res: res.append([ni, nj, nk])
                nums_dict[nk] = j
        return res
        """
        
        # 7th solution: two-pointer with binary search [accepted] see
        # https://leetcode.com/problems/3sum/discuss/7653/Python-solution-.
        # https://docs.python.org/3/library/bisect.html
        # All though still O(n^2) time complexity, its iteration times is far less!
        """
        nums, res, n = sorted(nums), [], len(nums)
        for i in range(n-2):
            if nums[i] > 0: break
            if i and nums[i] == nums[i-1]: continue
            hi = n - 1
            # binary search
            lo = bisect.bisect_left(nums, - nums[i] - nums[hi], i + 1, hi) - 1
            lo += (lo == i)
            # all possible values are bounded by lo and hi, then start checking
            while lo < hi:
                sum = nums[i] + nums[lo] + nums[hi]
                if sum == 0:
                    res += (nums[i], nums[lo], nums[hi]),
                    while lo < hi and nums[lo] == nums[lo+1]: #remove duplicate
                        lo += 1 
                    while lo < hi and nums[hi] == nums[hi-1]: #remove duplicate
                        hi -= 1
                lo += sum <= 0 # if sum < 0, need larger lo
                hi -= sum >= 0 # if sum > 0, need smaller hi
        return res
        """
        
        # 8th solution: if bisect module is not used:
        nums, res, n = sorted(nums), [], len(nums)
        for i in range(n-2):
            if nums[i] > 0: break
            if i and nums[i] == nums[i-1]: continue
            hi = n - 1
            # binary search
            # lo = bisect.bisect_left(nums, - nums[i] - nums[hi], i + 1, hi) - 1
            lo = self.bisect(nums, -nums[i]-nums[hi], i+1, hi) - 1
            lo += (lo == i)
            # all possible values are bounded by lo and hi, then start checking
            while lo < hi:
                sum = nums[i] + nums[lo] + nums[hi]
                if sum == 0:
                    res += (nums[i], nums[lo], nums[hi]),
                    while lo < hi and nums[lo] == nums[lo+1]: #remove duplicate
                        lo += 1 
                    while lo < hi and nums[hi] == nums[hi-1]: #remove duplicate
                        hi -= 1
                lo += sum <= 0 # if sum < 0, need larger lo
                hi -= sum >= 0 # if sum > 0, need smaller hi
        return res
        
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
        
        
        # 2nd solution: time limit exceeded
        # 3rd solution: 7392 ms (5%), 18.8 MB (10%)
        # 4th solution: 6636 ms (6%), 18.7 MB (12%)
        # 5th solution: 5932 ms (8%), 18.6 MB (14%)
        # 6th solution: 4072 ms (18%), 17.9 MB (31%)
        # 7th solution: 720 ms (87%), 17 MB (94%) !!!
        # 8th solution: 732 ms (86%), 17 MB (94%)
