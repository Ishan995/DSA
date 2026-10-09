class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        result = []
        
        # 1. Fix the first number
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicate for the first number
                
            # 2. Use two pointers for the remaining two numbers
            left = i + 1
            right = n - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
                    # Skip duplicates for left and right pointers
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                        
                elif total < 0:
                    left += 1   # Sum is too small, move left up
                else:
                    right -= 1  # Sum is too big, move right down
                    
        return result
        