class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        n = len(s)
        m = len(t)
        ind = -1
        if (m < n):
            return False
        for i in range(n):
            if (ind >= m-1):
                return False
            smaller = s[i:i+1]
            # print(ind, m)
            for j in range(ind + 1, m):
                bigger = t[j:j+1]
                if (smaller == bigger):
                    ind = j
                    break
                ind = j
            if (ind >= m-1 and smaller != bigger):
                return False
                # print(i, j, smaller, bigger, m)
            # return False
        return True 