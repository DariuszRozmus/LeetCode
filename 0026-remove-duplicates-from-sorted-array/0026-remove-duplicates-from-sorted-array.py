class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        T = []
        if (len(nums) > 0):
            T.append(nums[0])
        for i in range(1,len(nums)):
            if (nums[i] != T[len(T)-1]):
                T.append(nums[i])
        k = len(T)
        for i in range(k):
            nums[i] = T[i]
        return k