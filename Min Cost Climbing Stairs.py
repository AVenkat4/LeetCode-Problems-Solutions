class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        
        n = len(cost)
        dp = [0]*(n+1)
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, n+1):
            dp[i] = min(dp[i-1], dp[i-2]) 
            dp[i] += (cost[i] if i != n else 0)
        
        return dp[n]