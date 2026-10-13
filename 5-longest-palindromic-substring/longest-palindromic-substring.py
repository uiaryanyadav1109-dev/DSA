class Solution:
    def longestPalindrome(self, s: str) -> str:
        strn = ""
        strn_len=0
        
        for i in range(len(s)):
            #for odd length
            l, r = i, i
            while l>=0 and r <len(s) and s[l] == s[r]:
                if (r-l+1) > strn_len:
                    strn = s[l:r+1]
                    strn_len = r-l + 1    
                l -= 1
                r += 1
            #for even length
            l, r = i, i+1
            while l>=0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > strn_len:
                    strn = s[l:r+1]
                    strn_len= r - l + 1
                l -=1
                r +=1
        return strn