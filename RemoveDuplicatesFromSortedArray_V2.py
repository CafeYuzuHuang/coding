class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 2021.04.08 revisited
        
        # 1st solution: datatype conversion, O(n)
        """
        try:
            assert nums != []
        except:
            return 0
        else:
            # Convert to set dtype to quarantee the uniqueness of each element, 
            # followed by sorting in ascenting order.
            nums[:] = sorted(set(nums)) # return of sorted() is list datatype
            return len(nums)
        """
        
        # 2nd solution: two-pointer, O(n)
        n = len(nums)
        if n == 0: return 0
        i = 0
        for j in range(n):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i+1 # nums[:i+1] is the part we want
        
        # 1st solution: 80 ms (80%) and 16.5 MB (5%)
        # 2nd solution: 84 ms (61%) and 15.9 MB (52%)
