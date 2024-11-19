from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_pre = strs[0]
        for string in strs:
            x = string
            k = 0
            while string.startswith(common_pre) == False:
                common_pre = common_pre[:-1]
            if not common_pre:
                return ""
        return "".join(common_pre)

l = ["flower", "flow", "flight"]
print(Solution().longestCommonPrefix(l))