class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
       
        dp=[0]*26
        for   ch in s:
            val=ord(ch)-ord('a')
            n=0
            for j in range(max(0,val-k),min(25,val+k)+1):
                n=max(n,dp[j])
            dp[val]=n+1
        return max(dp)        
          
               
        return max(dp)           

        
        