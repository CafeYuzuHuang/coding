class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # 2021.03.12
        # 1st solution: naive
        
        try:
            assert nums != []
        except:
            return 0
        while True:
            try:
                nums.remove(val)
            except:
                return len(nums)
        
        
        # 2nd solution: not to use list.remove method
        """
        try:
            assert nums != []
        except:
            return 0
        pos = len(nums) - 1
        while pos >= 0:
            try:
                assert val == nums[pos]
                nums.pop(pos)
            except:
                pass
            pos -= 1
        return len(nums)
        """
        # 1st solution runtime 16 ms (92%) and memory 13.2 MB (91%)
        # 2nd solution runtime 20 ms (73%) and memory 13.4 MB (67%)
        
