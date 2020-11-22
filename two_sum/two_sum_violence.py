from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx1, num1 in enumerate(nums):
            for idx2, num2 in enumerate(nums):
                if num2 == target - num1 and idx1 != idx2:
                    return idx1, idx2


if __name__ == '__main__':
    solution = Solution()
    print(solution.twoSum([1, 1], 2))
