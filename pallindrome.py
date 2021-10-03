class Solution:
    def isPalindrome(self, x: int) -> bool:

        strg = str(x)
        strrev = strg[::-1]
        if strg == strrev:
            return True
        else:
            return False
print(Solution().isPalindrome(345))
print(Solution().isPalindrome(111))