class Solution:
    def findMin(self, nums: List[int]) -> int:
                
       k=0
       for i in range (len(nums)):
           if nums[i]<nums[k]:
                k=i
       return nums[k]        
            