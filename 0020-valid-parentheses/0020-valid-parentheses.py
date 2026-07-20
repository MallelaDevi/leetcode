class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2!=0:
                return False
        b={')':'(','}':'{',']':'['}
        c=[]
        for i in s:
            if i in b:
              t=c.pop() if c else "#"
              if b[i]!=t:
                   return False
            else:
                c.append(i)
        return not c                

        

        