
def reverseString(s: [str]):
    """
    Do not return anything, modify s in-place instead.
    """
    left = 0
    right = len(s)-1
    while left<right:
        s[left],s[right]=s[right],s[left]
        left=left+1
        right-=1
    return s

print(reverseString(["H","e","l","l","o"]))