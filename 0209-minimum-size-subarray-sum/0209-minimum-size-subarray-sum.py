class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        sum1, ind_st, ind_sd = nums[0],0,0
        res = float('inf')
        while(ind_sd < n-1):
            # print(nums, nums[ind_sd], nums[ind_st], sum1)
            if sum1 >= target:
                res = min(res, ind_st - ind_sd + 1)

            if sum1 < target and ind_st < n-1:
                ind_st += 1
                sum1 += nums[ind_st]
            else:
                sum1 -= nums[ind_sd]
                ind_sd +=1
                ind_st = max(ind_sd, ind_st)

        if sum1 >= target:
            res = min(res, ind_st - ind_sd + 1)
            
            
        if res == float('inf'):
            return 0
        else:
            return res

        