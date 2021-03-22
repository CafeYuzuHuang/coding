class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 2021.03.22:
        # 1st solution: time complexity O(N^2) w/o extra memory
        """
        i = len(nums)-1
        while i > 0:
            try:
                assert nums[0] != nums[i]
                i -= 1
            except:
                nums.pop(i)
                nums.pop(0)
                i = len(nums)-1 # update
        return nums[0]
        """
        
        # 2nd solution: time complexity O(N), space O(N)
        """
        dict = {}
        for n in nums:
            try:
                assert dict[n] == 1
                dict[n] = False
            except:
                dict[n] = True
        for k in dict:
            if dict[k] is True:
                return k
        """
        
        # 3rd solution: time complexity O(N), space complexity O(1)
        # Use set to gather unique elements
        return 2*sum(set(nums)) - sum(nums)
        
        # 1st solution: 9208 ms (5%) and 15.2 MB (99%)
        # 2nd solution: 132 ms (37%) and 16.5 MB (10%)
        # 3rd solution: 108 ms (76%) and 16.2 MB (26%)
        
