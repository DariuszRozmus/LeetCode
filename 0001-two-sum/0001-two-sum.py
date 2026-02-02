class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num = nums.copy()
        nums.sort()
        n = len(nums)

        def binsearch(nums, target, first, last):

            if first > last:
                return -1
            center = first + (last-first)//2
            if nums[center] == target:
                return center
            elif nums[center] > target:
                return binsearch(nums,target, first, center-1)
            else: 
                return binsearch(nums,target, center+1, last)

        for i in range(n-1):
            val = nums[i]
            indx = binsearch(nums,target - val,i+1, n-1) 
            if indx != -1:
                val2 = nums[indx]
                res = []
                for j in range(n):
                    if num[j] == val:
                        res.append(j)
                        break
                for k in range(n):
                    if num[k] == val2 and k != res[0]:
                        res.append(k)
                        return res
