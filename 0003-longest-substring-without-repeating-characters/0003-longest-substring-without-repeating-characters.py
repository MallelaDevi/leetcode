class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        ans=0
        for i in range(n):
            v=set()
            for j in range(i,n):
                if s[j] in v:
                    break
                else:
                    v.add(s[j])
                    ans=max(ans,j-i+1)
        return ans                
          
        return ans        


        