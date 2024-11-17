from typing import List, Dict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m: Dict[int, int] = {}
        sol = []
        for i in range(len(nums)):                
            if nums[i] in m:
                sol.extend([i, m[nums[i]]])
                return sol
            else:
                comp = target - nums[i]
                m[comp] = i
                i += 1

if __name__ == "__main__":
    sol = Solution()

    print(sol.twoSum([15, 2, 7, 11], 9))