class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
    
        tmin = prices[0]
        T_max = [prices[n-1]]*n
        
        for i in range(n-2,-1,-1):
            T_max[i] = max(T_max[i+1],prices[i])
        # print(T_max)
        
        result = max(0, T_max[0]-tmin)

        for i in range(1,n):
            if(tmin > prices[i]):
                tmin = prices[i]
                result = max(result, T_max[i]-tmin)
        return result