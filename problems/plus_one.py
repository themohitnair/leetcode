from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        digits[0] += 1
        for i in range(len(digits) - 1):
            if digits[i] > 9:
                digits[i + 1] += (digits[i] // 10)
                digits[i] %= 10                
            else:
                break
        if digits[len(digits) - 1] > 9:
            digits[len(digits) - 1] %= 10
            digits.append(1)
        return digits[::-1]