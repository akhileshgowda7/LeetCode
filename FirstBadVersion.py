# You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.
#
# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.
#
# You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

class Solution:
    def firstBadVersion(self,n, t)->int:
        left=0
        right=len(n)-1

        while left<right:
            mid=left+(right-left)//2
            if n[mid]==t:
                return n[mid-1]
            elif t<n[mid]:
                right=mid-1
            else:
                left=mid+1
        print(n[mid])
        return n[mid]
Solution().firstBadVersion([1,2,3,4,5,6,7,8,9,10],4)

