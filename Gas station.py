class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        '''
        n = len(gas)
        for i in range(0, n):
            sum = 0
            flag = 0
            for j in range(0, n):
                index = (i + j) % n
                if gas[index] - cost[index] + sum < 0:
                    flag = 1
                    break
                sum += (gas[index] - cost[index])
            if flag == 0:
                return i
        
        return -1
        '''
        
        start, total, tank = 0, 0, 0
        n = len(gas)
        for i in range(n):
            tank += (gas[i] - cost[i])
            if tank < 0:
                start = i + 1
                total += tank
                tank = 0
        
        return (-1 if (total + tank) < 0 else start)
		
		