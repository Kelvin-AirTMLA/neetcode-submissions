class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0.0
        
        if n == 1:
            return x

        if n == 0:
            return 1.0

        if n < 0:
            return (x * self.myPow(1/x, abs(n - 1)))

        return x * self.myPow(x, n - 1)