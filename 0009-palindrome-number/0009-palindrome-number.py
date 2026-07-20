class Solution:
    def isPalindrome(self, x: int) -> bool:
       x1= str(x)[::-1]
       if str(x)==x1:
        print(x,x1)
        return True
       else:
            print(x,x1)
            return False    

        