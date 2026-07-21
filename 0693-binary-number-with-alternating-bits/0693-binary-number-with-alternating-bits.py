class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        val = n ^ (n >> 1)
        return (val & (val + 1)) == 0

   

            
        