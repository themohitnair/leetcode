class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n *= -1
        res = 1
        while n > 0:
            if n % 2 != 0:
                res *= x
            n //= 2
            x *= x
        return res        

print(Solution().myPow(0.000000001, 227836783))