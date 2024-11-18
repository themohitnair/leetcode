class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x < 10:
            return True
        rev = 0
        temp = x
        while temp:
            rev = 10 * rev + (temp % 10)
            temp = temp // 10
        if rev == x:
            return True
        return False