class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort(reverse = True)
        n = len(people)
        i = 0
        num_boat = 0
        '''
        print(people)
        while i < n:
            cur = limit
            while i < n and cur >= people[i]:
                cur -= people[i]
                i += 1
            num_boat += 1
            print(i, num_boat)
        '''
        beg, end = 0, n - 1
        while beg <= end:
            if people[beg] + people[end] <= limit:
                end -= 1
            beg += 1
                
        return beg