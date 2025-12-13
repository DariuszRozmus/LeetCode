class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        T = []
        n = len(s)
        for i in range(n):
            if (s[i] == '('):
                T.append('(')
            elif (s[i] == '['):
                T.append('[')
            elif (s[i] == '{'):
                T.append('{')
            #
            elif len(T) < 1:
                return False
            elif (s[i] == ')'):
                ch = T.pop()
                if (ch != '('):
                    return False
            elif (s[i] == ']'):
                ch = T.pop()
                if (ch != '['):
                    return False
            elif (s[i] == '}'):
                ch = T.pop()
                if (ch != '{'):
                    return False
        if len(T) != 0:
            return False
        return True
