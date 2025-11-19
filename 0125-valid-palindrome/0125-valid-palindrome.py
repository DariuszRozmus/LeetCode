class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        p = s.lower()
        n = int(len(s))
        T = []
        for i in range(n):
            if ((ord(str(p[i:i+1])) >= ord(str("a")) and ord(str(p[i:i+1])) <= ord(str("z"))) or
            (ord(str(p[i:i+1])) >= ord(str("0")) and ord(str(p[i:i+1])) <= ord(str("9")))):
                T.append(str(p[i:i+1]))
        m = int(len(T)/2)
        # print(T)
        for i in range(m):
            if(T[i] != T[len(T) - 1 - i]):
                # print(T[i], T[len(T) - 1 - i], i)
                return False
        return True