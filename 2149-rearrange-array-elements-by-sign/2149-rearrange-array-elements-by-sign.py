class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        val=[]
        val1=[]
        res=[]
        for i in nums:
            if i<0:
                val.append(i)
            else:
                val1.append(i)
        for i in  range (len(val)):
            res.append(val1[i])
            res.append(val[i])
        return res    

                        

        