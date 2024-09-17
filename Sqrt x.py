class Solution:

    
    def mySqrt(self, x: int) -> int:
        if x==0:
            return 0
        else:

            L = int(2/(1/x + 1))
            R = (x+1)//2 
            while L<=R:
                M=(L+R)//2
                if M*M < x:
                    L = M+1
                elif M*M > x:
                    R = M-1
                else:
                    return M
            return R
        
