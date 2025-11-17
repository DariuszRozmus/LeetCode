class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        n = len(prices)
        if (n <= 1):
            return 0 
        T = [[0]*4 for j in range(n)]
    
        T[0][0] -= prices[0]

        T[1][0] -= prices[1]
        T[1][1] = max(T[0][0] + prices[1], 0)
        T[1][2] = T[0][0]
        T[1][3] = 0

        if n == 2:
            return max(T[1][0], T[1][1], T[1][2], T[1][3],0)
        
        for i in range(2,n):
            T[i][1] = max(T[i-1][0] + prices[i], T[i-1][2] + prices[i], T[i-1][1])
            ###
            T[i][0] = max(T[i][1] - prices[i], T[i-1][1] - prices[i], T[i-1][3] - prices[i])
            T[i][2] = T[i-1][0]
            T[i][3] = T[i-1][1]
        print T
        return max(T[n-1][0], T[n-1][1], T[n-1][2], T[n-1][3],0)
             