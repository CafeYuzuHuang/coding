class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 2021.03.23
        # To find the leader element which appears more than n/2 times
        
        # 1st solution: golden solution taught by "codility"
        # time complexity O(N), space complexity O(1)
        # e.g. for [2, 2, 1, 1, 1, 2, 2]
        # []->[2]->[2,2]->[2]->[]->[1]->[]->[2]->candidate = 2
        """
        size = 0
        val = None
        for i, c in enumerate(nums):
            if size == 0:
                val = c
                size += 1
            else:
                if val != c:
                    size -= 1
                else:
                    size += 1
        # Since the majority is gueranteed to be existing
        # thus no further examination necessary
        return val
        """
        
        # 2nd solution: boosting the efficiency
        size = 0
        val = None
        for n in nums:
            try:
                assert size > 0
                try:
                    assert n != val
                    size -= 1
                except:
                    size += 1
            except:
                size += 1
                val = n
        return val
        
        # 1st: Time: 168 ms (63%), memory: 15.5 MB (82%)
        # 2nd: Time: 168 ms (63%), memory: 15.6 MB (10%)
