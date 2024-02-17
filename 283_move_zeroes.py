'''
https://leetcode.com/problems/move-zeroes/
'''
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        arr_temp = [] #here I'll add zeroes
        i = 0
        #find all zeroes and replace them in arr_temp
        while i < len(nums):
            if nums[i] == 0:
                nums.pop(i)
                arr_temp.append(0)
            else:
                i += 1
                
        nums.extend(arr_temp) #add zeroes in the end of nums
        #return nums (optional)