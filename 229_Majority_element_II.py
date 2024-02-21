'''
https://leetcode.com/problems/majority-element-ii
Runtime: 70 ms
Memory: 12.79 Mb
'''
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        majority_elements = [x for x in set(nums) if nums.count(x) > len(nums)//3]
        return majority_elements