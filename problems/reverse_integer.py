class Solution:
    def reverse(self, x: int) -> int:
        INT32_MIN = -2**31
        INT32_MAX_PLUS_ONE_LOL = 2**31
        neg = 0
        if abs(x) < 10:
            return x
        if x < 0:
            neg = 1
            x *= -1        
        rev = 0
        while x:
            rev = 10 * rev + (x % 10)
            x = x // 10
        if neg == 1:
            rev *= -1

        if rev not in range(INT32_MIN, INT32_MAX_PLUS_ONE_LOL):
            rev = 0
        return rev

print(Solution().reverse(-123))