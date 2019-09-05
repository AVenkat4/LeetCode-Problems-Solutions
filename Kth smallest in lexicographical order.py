class Solution(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        def calcSteps(n, n1, n2):
            steps = 0
            while n1 <= n:
                steps += min(n2, n + 1) - n1
                n1 *= 10
                n2 *= 10
            return steps
        
        cur = 1
        k -= 1
        while k > 0:
            steps = calcSteps(n, cur, cur + 1)
            if steps <= k:
                k -= steps
                cur += 1
            else:
                k -= 1
                cur *= 10
        return cur
        
        