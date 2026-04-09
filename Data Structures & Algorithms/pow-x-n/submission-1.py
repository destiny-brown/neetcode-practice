class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        if n < 0:
            return 1.0 / self.myPow(x, -n)
        
        if n % 2 == 0:
            call = self.myPow(x, n//2)
            return call * call
        
        else:
            call = self.myPow(x, n//2)
            return x * call * call 
        
