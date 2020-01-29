class Solution(object):
    def addNegabinary(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        lookup = {-2: (0,1), -1:(1,1), 0:(0, 0), 1:(1, 0), 2:(0, -1), 3:(1, -1)}
        size = max(len(arr1), len(arr2)) 
        result = []
        carry = 0
        while len(arr1) > 0 or len(arr2) > 0:
            a, b = 0, 0
            if len(arr1) > 0:
                a = arr1.pop()
            if len(arr2) > 0:
                b = arr2.pop()
            
            sum_ = a + b + carry
            res, carry = lookup[sum_]
            result.append(res)
            
        while carry != 0:
            res, carry = lookup[carry]
            result.append(res)
        
        while len(result) > 1 and result[-1] == 0:
            result.pop()
            
        return result[::-1]