class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        ordered_line = []
        insertion_order = sorted(people, key = lambda (h,k):(-h, k))
        for p in insertion_order:
            ordered_line.insert(p[1], p)
        
        return ordered_line