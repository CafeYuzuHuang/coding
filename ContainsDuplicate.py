class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # 2021.03.29
        # 1st and 2nd solution: sorting, time O(nlogn), space O(n)
        """
        # nums = sorted(nums) # 1st
        nums.sort() # 2nd
        for i, c in enumerate(nums[:-1]):
            if c == nums[i+1]: return True
        return False
        """
        
        # 3rd solution: datatype conversion / python's trick
        """
        return True if len(set(nums)) < len(nums) else False
        """
        
        # 5th solution: hash table (for comparison)
        if len(nums) < 2: return False
        rec = {}
        for n in nums:
            try:
                assert n in rec
                return True
            except:
                rec[n] = 1
        return False
        # time: O(n); for n searches, each O(1)
        # space: O(n); but only keys used, not efficient at all.
        
        # 1st solution: 120 ms (59%), 19.1 MB (93%)
        # 2nd solution: 132 ms (15%), 19.1 MB (93%)
        # 3rd solution: 108 ms (97%), 20.2 MB (66%)
        # 5th solution: 116 ms (78%), 21.4 MB (26%)
        
