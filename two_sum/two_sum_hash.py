from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = {}
        for i, num1 in enumerate(nums):
            num2 = target - num1
            if num2 in hashtable:
                return [hashtable[num2], i]
            hashtable[num1] = i


if __name__ == '__main__':
    solution = Solution()
    print(solution.twoSum([1, 1], 2))
