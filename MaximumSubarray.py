
# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
#
# A subarray is a contiguous part of an array.


class Solution:
    def maxSubArray(self, nums:[int]) -> int:

        maxi, sum = nums[0], nums[0]
        for i in range(1, len(nums)):
            if (sum + nums[i] > nums[i]):
                sum += nums[i]
            else:
                sum = nums[i]
            maxi = max(maxi, sum)
        return maxi

print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))