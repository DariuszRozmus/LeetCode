class Solution(object):
    def merge(self, nums1, m, nums2, n):
        T = [-1]*(m+n)
        print(T)
        j,k = 0,0
        inf = float('inf')
        for i in range(m,m+n):
            nums1[i] = inf
        for i in range(m+n):
            if(len(nums1) > 0 and len(nums2) > 0):
                    if (nums1[j] <= nums2[k]):
                        T[i] = nums1[j]
                        j += 1
                        nums1.append(inf)
                    else:
                        T[i] = nums2[k]
                        k += 1
                        nums2.append(inf)
            elif(len(nums1) == 0 or len(nums2) == 0):
                if (len(nums2) == 0):
                    T[i] = nums1[j]
                    j += 1
                    nums2.append(inf)
                else:
                    pass
            else:
                pass
        for i in range(len(T)):
            nums1[i] = T[i]
        for i in range(len(nums1)-len(T)):
            nums1.pop()