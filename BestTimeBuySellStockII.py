class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 2021.03.22
        # 1st solution: Dynamic Programming, both time & space complexity are O(N)
        # The max profit is to capture all upward trend as possible
        
        n = len(prices)
        gain = 0
        if n <= 1: return 0
        for i in range(1, n):
            gain += max(0, prices[i]-prices[i-1])
        return gain
        
        # 1st solution: 48 ms (52%) and 14.7 MB (17%)
        # 2nd solution:
        
        
        
