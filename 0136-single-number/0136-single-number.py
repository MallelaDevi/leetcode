class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # d={}
        # for val in nums:
        #     d[val]=d.get(val,0)+1
        # for key,value in  d.items():
        #     if  val==1:
        #         val.append(key)
        # return key        
        xor=nums[0]
        for i in range(1,len(nums)):
            xor ^= nums[i]
        return xor
        