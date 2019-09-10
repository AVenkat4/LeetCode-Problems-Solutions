class Solution(object):
    def maxProfit(self, prices):
        
        n = len(prices)
        min_val = float('inf')
        max_diff = 0
        prev_diff = 0
        prev_minval = float('inf')
        
        profit = 0
        for i in range(n-1):
            if prices[i] < prices[i+1]:
                profit += prices[i+1] - prices[i]
        
        return profit
                