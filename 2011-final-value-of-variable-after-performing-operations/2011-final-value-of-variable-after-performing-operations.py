class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x=0
        for n in operations:
            if '+' in n:
                x+=1
            else:
                x-=1
        return x            
        