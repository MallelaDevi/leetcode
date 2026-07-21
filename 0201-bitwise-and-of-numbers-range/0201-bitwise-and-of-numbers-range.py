class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        ans=0
        while(left<right):
            right=right&right-1
        return right    
        # for i in range(left,right):

        