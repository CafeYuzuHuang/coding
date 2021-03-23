class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 2021.03.23
        # unique solution gueranteed
        # nums is sorted, members may be negative
        
        # 1st solution: the best solution for TwoSum
        # time complexity O(N), space O(N)
        """
        nums_dict = {}
        for i, num in enumerate(numbers):
            tmp = target - num
            try:
                # two indices are different and tmp in dict
                cc = nums_dict[num]
                if i != cc:
                    return [i+1, cc+1] if i < cc else [cc+1, i+1]
            except:
                pass
            nums_dict[tmp] = i
        return [0, 0] # solution not found!
        """
        
        # 2nd solution: two-pointer approach
        # time complexity O(N), space O(1)
        if len(numbers) == 2: return [1, 2] # edge case
        upper = len(numbers)-1
        lower = 0
        while upper > lower:
            tmp = target - numbers[upper]
            if numbers[lower] == tmp:
                return [lower+1, upper+1]
            elif numbers[lower] > tmp:
                upper -= 1
            else:
                lower += 1
        return[0, 0] # not found
        
        # 1st solution: 52 ms (38%) and 13.6 MB (72%)
        # 2nd solution: 40 ms (96%) and 13.6 MB (49%)
        
        
