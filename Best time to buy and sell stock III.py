class Solution(object):
    def maxProfit(self, prices):
        
        n = len(prices)
        oneBuy = float('inf')
        oneBuyoneSell = 0
        twoSell = float('inf')
        twoBuytwoSell = 0
        
        for p in prices:
            oneBuy = min(oneBuy, p)
            oneBuyoneSell = max(oneBuyoneSell, p - oneBuy)
            twoSell = min(twoSell, p - oneBuyoneSell)
            twoBuytwoSell = max(twoBuytwoSell, p - twoSell)
        
        return twoBuytwoSell
        