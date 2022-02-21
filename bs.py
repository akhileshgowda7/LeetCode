# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
#
# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
#
# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:
#
# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:
#
# Input: nums = [1,3,5,6], target = 7
# Output: 4

def searchInsert(nums:[], target: int) -> int:
    left = 0
    right = len(nums) - 1
    # print(right)
    # print(mid)
    while left < right:
        mid=left+(right-left)//2
        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1
    if target not in nums:
        return nums[mid]+1
    return nums[mid]


print(searchInsert([1,2,3,4,5,6,7,8],9))