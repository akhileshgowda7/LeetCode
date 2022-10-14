class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arry = []
        sum = 0
        for i in range(len(nums)):
            sum = sum+nums[i]
            arry.append(sum)
        
        return arry