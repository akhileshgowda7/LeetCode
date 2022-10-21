class Solution:
     def longestPalindrome(self, s):
        ans = 0
        hashmap = {}
        for i in range(len(s)):
            if s[i] in hashmap:
                hashmap[s[i]]+=1
            else:
                hashmap[s[i]] = 1
        numberOfSingle = 0
        for v in hashmap.values():
            if v > 1:
                if v % 2 ==0:
                    ans+= v
                else:
                    numberOfSingle +=1
                    ans+=v-1
            else:
                numberOfSingle +=1
        if numberOfSingle >=1:
            ans+=1
        return ans