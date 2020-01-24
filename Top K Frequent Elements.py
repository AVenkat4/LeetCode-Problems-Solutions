class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hs = collections.defaultdict(int)
        for i in nums:
            hs[i] += 1
        
        freq = {}
        for z,v in hs.iteritems():
            if v not in freq:
                freq[v] = [z]
            else:
                freq[v].append(z)
        
        arr = []
        for i in range(len(nums), -1, -1):
            if i in freq:
                
                for elem in freq[i]:
                    arr.append(elem)
        
        #print(arr)
        return [arr[x] for x in range(0, k)]