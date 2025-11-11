class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        result = 0
        T_min = [prices[0]]*n
        T_max = [prices[n-1]]*n
        for i in range(1,n):
            T_min[i] = min(T_min[i-1], prices[i])
        for i in range(n-2,0,-1):
            T_max[i] = max(T_max[i+1],prices[i])
        # print(T_min)
        # print(T_max)
        result = 0
        for i in range(n):
            result = max(T_max[i]-T_min[i],result)
        return result