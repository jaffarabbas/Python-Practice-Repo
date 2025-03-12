from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        map = {}
        for num in nums:
            if num in map:
                map[num] += 1
            else:
                map[num] = 1
        for key in map:
            if map[key] > len(nums) // 2:
                return key
            


nums = [3,2,3]
sol = Solution()
print(sol.majorityElement(nums)) # Expected output: 2