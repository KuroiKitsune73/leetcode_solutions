'''
https://leetcode.com/problems/fibonacci-number
Runtime:579ms
Memory:11.59 Mb
'''
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=1:
            return n
        if n>1:
            return self.fib(n-1)+self.fib(n-2)