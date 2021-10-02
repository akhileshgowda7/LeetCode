class Solution:
    def reverse(self,x:int)->int:
        if x>=2**21-1 or x<=-2**31:return 0
        else:
            strg=str(x)
            if x>0:
                revst=strg[::-1]
            else:
                temp=strg[1::]
                temp1=temp[::-1]
                revst="-" + temp1

            if int(revst) >= 2 ** 31 - 1 or int(revst) <= -2 ** 31:
                return 0
            else:
                return int(revst)

print(Solution().reverse(123))