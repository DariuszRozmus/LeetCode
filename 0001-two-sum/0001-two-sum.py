class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num = nums.copy()
        nums.sort()
        n = len(nums)

        def binserch(nums, target, first, last):

            if first > last:
                return -1
            center = first + (last-first)//2
            if nums[center] == target:
                return center
            elif nums[center] > target:
                return binserch(nums,target, first, center-1)
            else: 
                return binserch(nums,target, center+1, last)

        for i in range(n-1):
            val = nums[i]
            ntarget = target - val
            nind = binserch(nums,ntarget,i+1, n-1) 
            if nind != -1:
                val2 = nums[nind]
                res = []
                for j in range(n):
                    if num[j] == val:
                        res.append(j)
                        break
                for k in range(n):
                    if num[k] == val2 and k != res[0]:
                        res.append(k)
                        return res
