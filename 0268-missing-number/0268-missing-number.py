class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # nums.sort()
        # for i in range(1,len(nums)):
        #     if nums[i]!=i:
        #         return i
        # return len(nums)  
      
        n = len(nums)
        expected = n * (n + 1) // 2
        actual = sum(nums)
        return expected - actual      
        # n=len(nums)
        # for val in  range(len(nums)):
        #     xor ^= val^nums[val]
        # return xor    

        