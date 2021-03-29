class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # 2021.03.29
        # 2nd solution: naive
        """
        if not nums: return nums
        elif len(nums) == 1: return [str(nums[0])]
        summary = []
        x = nums[0]
        for i, c in enumerate(nums[:-1]):
            if nums[i+1] - 1 > c:
                summary.append(self.outputRange(x, c))
                x = nums[i+1]
        summary.append(self.outputRange(x, nums[-1]))
        return summary
    
    def outputRange(self, n1, n2):
        s = str(n1)
        if n2 != n1:
            s += "->" + str(n2)
        return s
        """
        
        # 3rd solution: optimized
        if not nums: return nums
        elif len(nums) == 1: return [str(nums[0])]
        summary = []
        x = nums[0]
        for i, c in enumerate(nums[1:]):
            d = nums[i] # i starts from 0
            try:
                assert c - 1 == d
            except:
                s = str(x) + "->" + str(d) if x != d else str(x)
                summary.append(s)
                x = c
        d = nums[-1]
        s = str(x) + "->" + str(d) if x != d else str(x)
        summary.append(s)
        return summary
        
        # 2nd solution: 32 ms (54%) and 14.3 MB (18%)
        # 3rd solution: 24 ms (95%) and 14.2 MB (79%)
        
