class Solution:
    def isPalindrome(self, x: int) -> bool:
        s=str(x)
        rev=s[::-1]
        if (s==rev):
            return True
        else:
            return False
        if rev<=-2**31 or rev>=-2**31:
            return 0
        else:
            return rev