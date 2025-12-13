class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()
        n = len(citations)
        i = 0
        result = 0
        while (result <= (n-i)):
            # print(min(citations[i], n-i))
            if (result < min(citations[i], n-i)):
                # print('s')
                result = min(citations[i], n-i)
            i += 1
            if (i >= n):
                break
        return result 
