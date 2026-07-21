class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        # val = n ^ (n >> 1)
        # return (val & (val + 1)) == 0
         l=[]
         while (n!=0):
            val=n%2
            l.insert(0,val)
            n=n//2  
         for i in range(1,len(l)):
            if(l[i-1]==l[i]):
               return False
         return True 

   

            
        