'''
https://leetcode.com/problems/power-of-three
'''

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        for i in range(32):
            res=3**i
            if res==n:
                return True
        else:
            return False