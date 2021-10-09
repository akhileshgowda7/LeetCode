# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
#
# You must write an algorithm with O(log n) runtime complexity.


class Solution:
    def SearchInsertPosition(self,nums,target)->int:
        left =0
        right = len(nums)-1

        while left<right:
            mid = left + (right-left) // 2
            if nums[mid]==target:
                return mid
            if target>nums[mid]:
                left=mid+1
            else:
                right=mid-1
        return left


print(Solution().SearchInsertPosition([1,2,3,5,6,7,9,10],4))