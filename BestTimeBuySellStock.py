class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 2021.03.22
        # Buy first, then close the position
        # Only long position allowed; short is prohibited
        # 1st solution: brute force
        # day  ------------------------------ 
        # act1 |<-  buy  ->| |<-   sell   ->|
        # act2 |<-    buy    ->| |<- sell ->|
        # tuning the day range to search best-buy-price (bbp) and 
        # best-sell-price (bsp) to maximize gain = max(0, bsp - bbp)
        """
        n = len(prices)
        if n <= 1: return 0
        gain = 0
        bbp = 10000
        bsp = 0
        for i in range(n-1):
            bbp = min(prices[0:i+1]) if i > 0 else prices[0]
            bsp = max(prices[i+1:-1]) if i < n-2 else prices[-1]
            gain = max(gain, bsp-bbp)
        return gain
        """
        
        # 2nd solution: to avoid time limit
        # for 1st solution, time complexity is O(N^2)
        # Here use divide-and-conquer method
        # time complexity: O(N*logN)
        """
        n = len(prices)
        if n <= 1: return 0
        mid = n//2
        return max( max(prices[mid:])-min(prices[:mid]),
                  self.maxProfit(prices[mid:]),
                  self.maxProfit(prices[:mid]))
        """
        
        # 8th solution: seems to need reducing time complexity to O(N)
        # One-pass solution: keep replace gain to maximize it
        # (r.f. problem 53 and the solution)
        """
        n = len(prices)
        bp = 10000
        gain = 0
        for i in range(n):
            if prices[i] < bp:
                bp = prices[i]
            elif prices[i] - bp > gain:
                gain = prices[i] - bp
        return gain
        """
        
        # 9th solution:
        bp = 10000
        gain = 0
        for i, p in enumerate(prices):
            try:
                assert p < bp
                bp = p
            except:
                try: 
                    assert p-bp < gain
                except:
                    gain = p - bp
        return gain
        
        # 1st solution: time limit exceed
        # 2nd solution: 1740 ms (5%) and 22.9 MB (11%)
        # 8th solution: 812 ms (60%) and 23 MB (11%)
        # 9th solution: 1088 ms (11%) and 22.9 MB (11%)
        
        
