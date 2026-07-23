class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans=0
        curr=prices[0]
        for i in range(1,len(prices)):
            
                curr=min(prices[i],curr)
                ans=max(prices[i]-curr,ans)
        return ans        
                
        