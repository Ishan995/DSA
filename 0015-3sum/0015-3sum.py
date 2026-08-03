class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):

            # Skip duplicate values for the first number
            if i > 0 and a == nums[i - 1]:
                continue

            # Two pointers
            l = i + 1
            r = len(nums) - 1

            while l < r:

                total = a + nums[l] + nums[r]

                if total > 0:
                    r -= 1

                elif total < 0:
                    l += 1

                else:
                    res.append([a, nums[l], nums[r]])

                    l += 1

                    # Skip duplicate second numbers
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        return res