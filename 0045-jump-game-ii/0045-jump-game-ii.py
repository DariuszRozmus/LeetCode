class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n =len(nums)
        T = [float('inf')]*n
        T[0] = 0
        for i in range(n):
            dist = nums[i]
            for j in range(1,dist+1):
                poz = min(i+j,n-1)
                T[poz] = min(T[poz],T[i]+1)
        return(T[n-1])