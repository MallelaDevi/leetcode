class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        val=0
        val1=0
        for i in range(len(nums)):
           val=(val^nums[i])&~val1
           val1=(val1^nums[i])&~val
        return val   



    

           


        