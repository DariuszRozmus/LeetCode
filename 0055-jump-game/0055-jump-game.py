class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        res = 0
        for i in range(n):
            res = max(res, i + nums[i])
            if (res >= (n-1)):
                return True
            if (res < (i+1)):
                return False
        