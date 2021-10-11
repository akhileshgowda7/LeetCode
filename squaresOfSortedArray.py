class Solution:
    def squaresOfSortedArray(self,nums)->[]:
        squares=[]
        for i in range(len(nums)):
            squares.append(nums[i]*nums[i])
        squares.sort()
        return squares
print(Solution().squaresOfSortedArray([-2,-3,4,8,5]))
