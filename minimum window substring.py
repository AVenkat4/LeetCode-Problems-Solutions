from collections import Counter
from collections import defaultdict
class Solution(object):
    def minWindow(self, s, t):
        # hashmap, missing, result - tuple, fast and slow ptr
        fast, begin = 0, 0
        missing = len(t)
        hmap = defaultdict(int)
        for c in t:
            hmap[c] += 1
        n = len(s)
        min_len = float('inf')
        start = 0
        while fast < n:
            if hmap[s[fast]] > 0:
                missing -= 1
            hmap[s[fast]] -= 1
            fast += 1
            while missing == 0:
                if min_len > (fast - begin):
                    min_len = fast - begin
                    start = begin
                if hmap[s[begin]] == 0:
                    missing += 1
                hmap[s[begin]] += 1
                begin += 1     
            print(missing, fast, begin, min_len)
        if min_len == float('inf'):
            return ""
        return s[start: start + min_len]
                
                    
                