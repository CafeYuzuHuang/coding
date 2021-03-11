class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 2021.03.11: Note negative integers might exist in nums!
        
        # 1st submission: Brute force solution: time complexity O(n^2)
        """
        # Generate index list before sorting by
        # sorting indices of nums by key = values of nums        
        n = len(nums)
        nums_sorted = sorted(nums)
        nums_s_ind = sorted(range(n), key = lambda k: nums[k])
        for i in range(len(nums_sorted)):
            for j in range(len(nums_sorted)):
                if nums_sorted[i] + nums_sorted[j] == target and i != j:
                    return [nums_s_ind[i], nums_s_ind[j]]
        return [-1, -1] # solution not found!
        """
        
        # 2nd submission: faster solution:
        """
        # Use dictionary comprehension, which might be helpful to reduce
        # space and time complexity.
        # Use reverse iteration trick to ensure two indices are different
        # if a = b = target/2
        n = len(nums)
        a_dict = {nums[i]: i for i in range(n)}
        b_dict = {target - nums[j]: j for j in range(n-1, -1, -1)}
        for k, v in a_dict.items():
            if k in b_dict:
                return [v, b_dict[k]]
        return [-1, -1] # solution not found!
        """
        
        # 3rd submission:
        # Fastest solution (?) (implemented after checking the solution :-D)
        """
        tmp = target - nums[0]
        nums_dict = {}
        nums_dict[tmp] = 0 # key: complementary; value: index in list
        for i in range(1, len(nums), 1):
            if nums[i] in nums_dict:
                return [i, nums_dict[nums[i]]]
            else:
                tmp = target - nums[i]
                nums_dict[tmp] = i
        return [-1, -1] # solution not found!
        """
        
        # 5th/6th submission: 3rd solution with sorting list in advance
        # -> slower and allocates more memory than 3rd ...
        # e.g. target = 100, sorted nums = [10, 90, 900, 998, 999, 1000]
        """
        n = len(nums)
        keys = sorted(nums) # in ascenting order
        values = sorted(range(n), key = lambda k: nums[k])
        tmp = target - keys[0] # largest complementary
        nums_dict = {}
        nums_dict[tmp] = values[0]
        for i in range(1, n, 1): # 6th: same results as 5th
        # for i in range(n-1, 0, -1): # 5th: loop starting from largest key
            if keys[i] in nums_dict:
                return [values[i], nums_dict[keys[i]]]
            else:
                tmp = target - keys[i]
                nums_dict[tmp] = values[i]
        return [-1, -1] # solution not found!
        """
        
        # 7th submission: "try" to improve 3rd
        """
        nums_dict = {}
        for i in range(len(nums)):
            tmp = target - nums[i]
            try:
                # two indices are different and tmp in dict
                if i != nums_dict[nums[i]]:
                    return [i, nums_dict[nums[i]]]
            except:
                pass
            nums_dict[tmp] = i
        return [-1, -1] # solution not found!
        """
        
        # 8th submission: "try" to improve 7th via enumerate
        # -> In conclusion, try-except is far faster than list operation,
        # -> besides, enumerate method allocates less memory than range method
        nums_dict = {}
        for i, num in enumerate(nums):
            tmp = target - num
            try:
                # two indices are different and tmp in dict
                if i != nums_dict[num]:
                    return [i, nums_dict[num]]
            except:
                pass
            nums_dict[tmp] = i
        return [-1, -1] # solution not found!
        
