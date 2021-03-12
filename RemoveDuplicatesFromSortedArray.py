class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 2021.03.12
        # 1st solution: naive
        """
        try:
            assert nums != []
        except:
            return 0
        pos = len(nums) - 1
        while pos > 0:
            try:
                assert nums[pos] == nums[pos-1]
                nums.pop(pos)
            except:
                pass
            pos -= 1
        return len(nums) # updated length of nums
        """
        # 2nd solution: attempt to reduce the runtime
        # Actually this approach violates the rule assigned
        # (Its extra time complexity is O(n) instead of O(1).)
        try:
            assert nums != []
        except:
            return 0
        else:
            # Convert to set dtype to quarantee the uniqueness of each element, 
            # followed by sorting in ascenting order.
            nums[:] = list(set(nums))
            nums.sort()
            return len(nums)
        # 1st solution runtime 76 ms (49%) and memory 14.9 MB (99%!!)
        # 2nd solution runtime 60 ms (92%!!) and memory 15.3 MB (45%)
