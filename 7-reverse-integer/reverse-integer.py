class Solution:
    def reverse(self, x: int) -> int:
        if(x>=0):
            val=int(str(x)[::-1])
        else:
            val=-(int(str(abs(x))[::-1]))
        if val<=-2**31 or val>=2**31:
            return 0
        else:
            return val