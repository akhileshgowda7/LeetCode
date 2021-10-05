class Solution:
    def isValid(self,s:str)->bool:
        bracket_map = {"(": ")", "[": "]", "{": "}"}
        open_parantheses = set(["(", "[", "{"])
        stack=[]
        for i in s:
            if i in open_parantheses:
                stack.append(i)
            elif stack and i==bracket_map[stack[-1]]:
                stack.pop()
            else:
                print("Invalid Argument")
                return False
        print("Valid Argument")
        return True


s = input("Please Enter the parantheses to check\n")
Solution().isValid(s)