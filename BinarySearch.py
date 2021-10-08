class solution:
    def binarySearch(self, nums:[] , target)->int:

        left=0
        right=len(nums)-1
        mid=(left+right)/2
        while left<right:
            mid=left+(right-left)//2
            if mid==target:
                return mid
            elif target<nums[mid]:
                right=mid-1
            else:
                left=mid+1
        return mid


print(solution().binarySearch([-1,0,3,5,9,12],9))


