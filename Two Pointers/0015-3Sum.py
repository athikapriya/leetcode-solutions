class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []

        for i in range(len(nums) -2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0 :
                    left += 1
                elif total > 0 :
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
            
        return result

"""
LeetCode 15. 3Sum

Pattern:
- Array
- Sorting
- Two Pointers

Approach:
1. Sort the array.
2. Fix one number.
3. Use two pointers to find the remaining two numbers.
4. Skip duplicates to avoid repeated triplets.

Time Complexity:
- Sorting: O(n log n)
- Two-pointer search: O(n²)
- Overall: O(n²)

Space Complexity:
- O(1) auxiliary
"""