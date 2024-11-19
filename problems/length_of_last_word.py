class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()[::-1]
        for i in range(len(s)):
            if s[i] == " ":
                break
        if i == (len(s) - 1):
            return len(s)
        s = s[:i]
        return len(s)