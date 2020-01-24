class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        lis = [0]*num_people
        epoch, flag = 0, 0
        while(candies > 0):
            for i in range(num_people):
                if candies < (epoch + i + 1):
                    flag = 1
                    lis[i] += candies
                    break
                lis[i] += (epoch + i + 1)
                candies -= (epoch + i + 1)
                #print(candies, lis)
            if flag == 1:
                break
            epoch += num_people
            

        return lis