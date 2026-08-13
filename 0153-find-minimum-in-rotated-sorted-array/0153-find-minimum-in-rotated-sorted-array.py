class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        while l<r:
            mid=(l+r)//2
            if (nums[mid]>nums[r]):
                l=mid+1
            else:
                r=mid
        return nums[l]           

                
    #    k=0
    #    for i in range (len(nums)):
    #        if nums[i]<nums[k]:
    #             k=i
    #    return nums[k]        
            