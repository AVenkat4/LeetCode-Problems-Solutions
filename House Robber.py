class Solution(object):
    def rob(self, nums):
        slow_sum = 0
        fast_sum = 0
        n = len(nums)
        for i in range(n):
            temp = fast_sum
            fast_sum = max(slow_sum + nums[i], fast_sum)
            slow_sum = temp
        return fast_sum
            
                
        