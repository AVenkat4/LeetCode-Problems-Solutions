class Solution(object):
    def jump(self, nums):
        n = len(nums)
        dp = [float('inf')]*n
        dp[0] = 0
        for i in range(n):
            if i + nums[i] < n and dp[i] + 1 > dp[nums[i] + i]:
                continue
            for j in range(1, nums[i] + 1):
                if i+j < n:
                    dp[i+j] = min(dp[i] + 1, dp[i+j])
            #print(dp)
        return dp[n-1]
                    
        