class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # 2021.03.30
        # c.f. problem 217: sorting and datatype conversion cannot be used
        # 2nd solution: hash table 
        """
        if k == 0: return False
        elif len(nums) <= 1: return False
        elif len(nums) <= 2:
            if nums[0] != nums[1]:
                return False
            else:
                return True
        rec = {}
        for i, n in enumerate(nums):
            try:
                assert rec[n] != i and abs(rec[n] - i) <= k
                return True
            except:
                rec[n] = i # replace the former recorded index
        return False
        """
        
        # 3rd solution: optimized
        rec = {}
        for i, n in enumerate(nums):
            try:
                assert rec[n] != i
                assert abs(rec[n] - i) <= k
                return True
            except:
                rec[n] = i # replace the former recorded index
        return False
        
        # 2nd solution: 96 ms (43%) and 21.8 MB (19%)
        # 3rd solution: 100 ms (27%) and 21.7 MB (35%)
        
