'''
https://leetcode.com/problems/power-of-four
'''
class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        for i in range(32):
            res=4**i
            if res==n:
                return True
        else:
            return False