class Solution:
    def mySqrt(self, x: int) -> int:
        g = x / 2
        while (abs(g * g - x) > 0.0001):
            g = (g + (x / g)) / 2
        return int(g)