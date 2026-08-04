class Solution:
    def reverseVowels(self, s: str) -> str:
        a='aeiouAEIOU'
        l=0
        s=list(s)
        r=len(s)-1
        while l<r:
            while (l<r and s[l] not in a):
                l=l+1
            while (l<r and s[r] not  in a):
                r=r-1
            s[l],s[r]=s[r],s[l]
            l+=1
            r-=1
        return "".join(s)   




 

        