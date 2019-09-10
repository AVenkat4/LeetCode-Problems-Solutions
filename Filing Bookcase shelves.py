class Solution(object):
    def minHeightShelves(self, books, shelf_width):
        
        n = len(books)
        dp = [0]*(n+1)
        
        dp[0] = 0
        for i in range(0, n):
            dp[i+1] = dp[i] + books[i][1]
            sum_, h = 0, 0
            for j in range(i,-1,-1):
                sum_ += books[j][0]
                if sum_ > shelf_width:
                    break
                else:
                    h = max(h, books[j][1])
                    dp[i+1] = min(dp[i+1], dp[j] + h)
        
        return dp[n]
        
        