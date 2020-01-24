class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def sort(nums):
            half = len(nums)/2
            if half:
                left = sort(nums[:half])
                right = sort(nums[half:])
                m, n = len(left), len(right)    
                i, j = 0, 0
                while i < m or j < n:
                    if j == n or i < m and left[i][1] <= right[j][1]:
                        nums[i+j] = left[i]
                        smaller[left[i][0]] += j
                        i += 1
                    else:
                        nums[i+j] = right[j]
                        j += 1
            return nums
        
        smaller = [0]*len(nums)
        sort(list(enumerate(nums)))
        
        return smaller