class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix=' '
        for i in strs:
            if(len(i)<len(prefix) or prefix==" "):
                prefix=i
        need=len(strs)
        count=0
        result=''
        while(need !=count):
            count=0
            for i in strs:
                if(prefix==i[:len(prefix)]):
                    count+=1
            result=prefix
            prefix=prefix[:-1]
        if(need==count):
            return result
        else:
            return ' '
