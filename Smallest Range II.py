class Solution(object):
    def smallestRangeII(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        n = len(A)
        min_a, max_a = float('inf'), -float('inf')
        
        A = sorted(A)
        first, last = A[0], A[-1]
        res = last - first
        for i in range(n - 1):
            maxi = max(A[i] + K, last - K)
            mini = min(A[i+1] - K, first + K)
            res = min(maxi - mini, res)
        return res
        