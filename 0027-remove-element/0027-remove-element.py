class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        T = []
        for i in range(len(nums)):
            if (nums[i] != val):
                T.append(nums[i])
        k = len(T)
        for i in range(k):
            nums[i] = T[i]
        return k
        