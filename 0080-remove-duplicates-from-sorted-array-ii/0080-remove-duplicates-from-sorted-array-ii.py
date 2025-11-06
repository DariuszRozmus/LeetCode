class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num = nums[0]
        indA = 1
        cntA = 1
        # b = 0
        for i in range(1,len(nums)):
            if (nums[i] == num):
                if(cntA < 2):
                    nums[indA] = nums[i]
                    cntA += 1
                    indA += 1
            else:
                nums[indA] = nums[i]
                cntA = 1
                indA += 1
                num = nums[i]
            # print(nums, "cntA", cntA, "indA", indA, "num", num)
        return indA
            
            
            
            
             
                    
        