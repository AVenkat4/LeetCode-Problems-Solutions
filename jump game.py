class Solution(object):
    def __init__(self,):
        self.val = False
        self.visited = []
    def canReach(self, nums, curInd, n):
        
        self.visited[curInd] = 1
        
        if curInd == n:
            return True
        if curInd > n or nums[curInd] == 0:
            return False
        for i in range(1, nums[curInd]+1):
            if self.visited[curInd + i] == 0:
                self.val = self.val | self.canReach(nums, curInd + i, n)
            if self.val == True:
                break
            #print(curInd, i, nums[curInd+i], self.val)
        
        return self.val
    
    def canJump(self, nums):
        n = len(nums)
        #self.visited = [0]*n
        #return self.canReach(nums, 0, n-1)
        farest = 0
        for i in range(0, n):
            if farest < i:
                return False
            farest = max(farest, i + nums[i])
        
        return True
        