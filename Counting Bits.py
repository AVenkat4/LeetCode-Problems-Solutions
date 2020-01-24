class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        
        
        lis = [0, 1, 1, 2]
        powtwo = [2**i for i in range(0, 30)]
        for i in range(4, num+1):
            if i in powtwo:
                lis2 = [x for x in lis]
                lis.extend([x+1 for x in lis2])
        
        return lis[:num+1]