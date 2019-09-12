class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        '''
        count = collections.defaultdict(int)
        maj_elem = nums[0]
        for i in range(n):
            count[nums[i]] += 1
            if count[nums[i]] > (n/2):
                maj_elem = nums[i]
                break
            
            
        return maj_elem'''
        count = 1
        maj_elem = nums[0]
        for i in range(1, n):
            if nums[i] == maj_elem:
                count += 1
            else:
                count -= 1
                if count <= 0:
                    maj_elem = nums[i]
                    count = 1
                
        return maj_elem