'''
https://leetcode.com/problems/remove-element/description/
Time: 20ms
Memory: 11.62 Mb
'''

class Solution(object):
    def removeElement(self, nums, val):    
        for i in range(len(nums)+1):
            if val in nums:
                nums.remove(val)
                i+=1
        print(len(nums))