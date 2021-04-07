class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 2021.04.07 revisited
        # length of nums >= 2, only exist one solution
        
        # 1st & 11th solution: one hash table
        
        rec = {}
        for i, n in enumerate(nums):
            tmp = target - n
            try: # past i, n -> j != i, tmp != n
                assert i != rec[tmp]
                return [rec[tmp], i] # indices in ascent order
            except:
                rec[n] = i
        # return [-1, -1] # no solution found
        
        
        # 2nd & 12th solution: comparative
        """
        rec = {}
        for i, n in enumerate(nums):
            if n in rec and i != rec[n]: return [rec[n], i]
            rec[target-n] = i
        # return [-1, -1] # no solution found
        """
        
        # 3rd solution: sorting + binary search
        # time complexity O(nlogn), space complexity O(n)
        """
        n = len(nums)
        keys = sorted(nums) # in ascenting order
        values = sorted(range(n), key = lambda k: nums[k])
        
        for i, c in enumerate(keys[:-1]):
            tmp = target - c
            j = self.bisect(keys, tmp, i+1, n-1,)
            if j >= 0: return [values[i], values[j]]
        # return [-1, -1] # no solution found
        """
        
        # 5th solution: sorting + binary search (optimized)
        """
        n = len(nums)
        nums_sorted = sorted(nums) # in ascenting order
        for i, c in enumerate(nums_sorted[:-1]):
            tmp = target - c
            j = self.bisect(nums_sorted, tmp, i+1, n-1,)
            if j >= 0: 
                if c == tmp: 
                    ii = nums.index(c)
                    return [ii, nums.index(c, ii+1)]
                else: 
                    return [nums.index(c), nums.index(tmp)]
        # return [-1, -1] # no solution found
        """
        
        # 6th solution: two-pointer approach, see
        # https://leetcode.com/problems/two-sum/discuss/1058246/Iterative-using-binary-search-method
        """
        sorted_nums = sorted(nums)
        left = 0
        right = len(nums)-1
        while left < right:
            vl = sorted_nums[left]
            vr = sorted_nums[right]
            if vl+vr == target:
                il = nums.index(vl)
                ir = nums.index(vr, il+1) if vl == vr else nums.index(vr)
                return [il, ir]
            if vl+vr > target: right -= 1
            else: left += 1
        # return [-1, -1] # solution not found
        """
        
        # 7th & 13th solution: optimize 6th?
        """
        sorted_nums = sorted(nums)
        left = 0
        right = len(nums)-1
        while left < right:
            vl, vr = sorted_nums[left], sorted_nums[right]
            try:
                assert vl+vr == target
                il = nums.index(vl)
                ir = nums.index(vr, il+1) if vl == vr else nums.index(vr)
                return [il, ir]
            except:
                try:
                    assert vl+vr > target
                    right -= 1
                except:
                    left += 1
        # return [-1, -1] # solution not found
        """
        
        # 8th-10th solution: 5th optimized?
        """
        n = len(nums)
        nums_sorted = sorted(nums) # in ascenting order
        t = self.bisect(nums_sorted, target, 0, n-1, ret_mode = 'right') # target > min(nums)
        for i, c in enumerate(nums_sorted[:-1]):
            tmp = target - c
            if tmp > target:
                j = self.bisect(nums_sorted, tmp, t, n-1,)
            else:
                j = self.bisect(nums_sorted, tmp, i+1, t,)
            if j >= 0: 
                if c == tmp: 
                    ii = nums.index(c)
                    return [ii, nums.index(c, ii+1)]
                else: 
                    return [nums.index(c), nums.index(tmp)]
        # return [-1, -1] # no solution found
        """
    
    def bisect(self, nums, target, low, high, ret_mode = 'none'):
        """
        Assume you don't know python has the built-in bisect module can be used.
        -> implement binary search by yourself.
        Args:
            nums is a list sorted in ascent order, all elements are int
            target, low, high are int
            low >= 0, high <= len(nums)-1
        Return: int
        """
        left, right = low, high
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target: return mid
            elif nums[mid] > target: right = mid - 1
            elif nums[mid] < target: left = mid + 1
        # crossed, i.e. left > right
        if ret_mode == 'left': return left
        elif ret_mode == 'right': return right
        else: return -1
        
        
        
        # 19th solution: 
        # (1) Judge if even or odd:
        # odd + odd & even + even = even
        # odd + even = odd
        # (2) Judge if unique:
        # If a1 + a2 = a3 + a4 = 2 -> target != 2
        # any element value will not appear more than twice
        # if a1 = a2 = a3 -> answer is not unique
        # if a1 = a2 -> only check if a1 + a2 = target
        
        """
        # a + b = target -> return index list [ia, ib]
        if target % 2 == 0:
            try: # A chance to solve it with O(1)
                halfTarget = target//2
                ia = nums.index(halfTarget)
                ib = nums.index(halfTarget, ia+1)
                return [ia, ib]
            except: 
                pass
        # Ensure a != b for a + b = target
        # If element ai is duplicated
        # -> ai and target - ai can be dropped out
        from collections import Counter
        rec = Counter(nums)
        for k, v in rec.items():
            if v == 1 and rec[target-k] == 1 and target-k != k: 
                return [nums.index(k), nums.index(target-k)]
        return [-1, -1] # solution not found
        """
        
        # 21th solution:
        # a + b = target -> return index list [ia, ib]
        """
        if target % 2 == 0:
            try: # A chance to solve it with O(1)
                halfTarget = target//2
                ia = nums.index(halfTarget)
                ib = nums.index(halfTarget, ia+1)
                return [ia, ib]
            except: 
                pass
        # Ensure a != b for a + b = target
        # If element ai is duplicated
        # -> ai and target - ai can be dropped out
        rec = {}
        for n in set(nums):
            try:
                tmp = rec[n]
                return [nums.index(n), nums.index(tmp)] # O(logn)
            except:
                rec[target-n] = n
        return [-1, -1] # solution not found
        """
                
        
        # 1st solution: 40 ms (95%), 14.2 MB (90%)
        # 2nd solution: 48 ms (58%), 14.5 MB (11%)
        # 3rd solution: 60 ms (9%), 14.5 MB (44%)
        # 5th solution: 48 ms (58%), 14.4 MB (44%)
        # 6th solution: 52 ms (17%), 14.5 MB (44%)
        # 7th solution: 52 ms (17%), 14.5 MB (11%)
        # 8th solution: 36 ms (99%), 14.4 MB (72%)
        # 9th solution: 60 ms (9%), 14.3 MB (90%)
        # 10th solution: 56 ms (10%), 14.6 MB (11%)
        # 11th solution: 44 ms (82%), 14.5 MB (44%)
        # 12th solution: 48 ms (58%), 14.3 MB (90%)
        # 13th solution: 56 ms (10%), 14.4 MB (72%)
        # ...
        # 19th: 40 ms (95%), 14.6 MB (11%)
        # 21th: 44 ms (82%), 14.6 MB (11%)
        
