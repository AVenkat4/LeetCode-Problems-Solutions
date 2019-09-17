class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m = len(s)
        n = len(t)
        
        if m != n:
            return False
        
        s_arr = [0]*26
        t_arr = [0]*26
        
        for char in s:
            s_arr[ord(char) - ord('a')] += 1
        
        for char in t:
            t_arr[ord(char) - ord('a')] += 1
        
        for i in range(26):
            if s_arr[i] != t_arr[i]:
                return False
        
        return True