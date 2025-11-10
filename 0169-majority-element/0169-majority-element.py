class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = nums[0]
        counts = {}
        max = 0
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        for key, value in counts.items():
            if value > max:
                max = value
                result = key
        return result