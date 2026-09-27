class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x<0 or (x%10==0 and x!=0)):
            return False
        elif x==0:
            return True
        rev=0
        while(x>rev):
            ld=x%10
            rev=rev*10+ld
            x=x//10
        if (x==rev or x==rev//10):
            return True
        else :
            return False