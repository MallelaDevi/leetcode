class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        w=0
        m1=0
    
        for i in  range(k):
            w+=nums[i]
        m1=w
        for  i in range(k,len(nums)):
            w=w-nums[i-k]+nums[i]
            
            m1=max(m1,w)
        return m1/k 


        # n=len(nums)-k+1
        # m=0
        # for i in range(n):
        #     sum1=sum(nums[i:k+i])
        #     avg=sum1/k
        #     m=max(m,avg)
        # return m    

        # m=0
        # for  val in range(n):
        #     t=0
        #     for val1 in range(val,k+val):
        #         t= t+nums[val1]
        #     a=t/k
        #     m=max(m,a)
        # return m    








       

                   
        
        