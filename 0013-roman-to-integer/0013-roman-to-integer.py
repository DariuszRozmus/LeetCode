class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        T = [0]*n
        res = 0
        for i in range(n):
            if s[i] == 'I':
                T[i] = 1
            if s[i] == 'V':
                T[i] = 5
            if s[i] == 'X':
                T[i] = 10
            if s[i] == 'L':
                T[i] = 50
            if s[i] == 'C':
                T[i] = 100
            if s[i] == 'D':
                T[i] = 500
            if s[i] == 'M':
                T[i] = 1000
        for i in range(n-1):
            if T[i] >= T[i+1]:
                res += T[i]
            else:
                res -= T[i]
        res += T[n-1]
        return res