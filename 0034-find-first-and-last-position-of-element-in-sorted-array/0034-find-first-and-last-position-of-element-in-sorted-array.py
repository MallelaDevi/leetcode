class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left=0
        right=len(nums)-1
        val=-1

        # finding left
        while left<=right:
            mid=(left+right)//2
            if (nums[mid]==target):
                val=mid
                right=mid-1
            elif(nums[mid]<target):
                left=mid+1
            else:
                right=mid-1
# finding right
        left=0
        right=len(nums)-1
        val1=-1

        while left<=right:
            mid=(left+right)//2
            if (nums[mid]==target):
                val1=mid
                left=mid+1
            elif(nums[mid]<target):
                left=mid+1
            else:
                right=mid-1 
        return [val,val1]               
           



            
        
        