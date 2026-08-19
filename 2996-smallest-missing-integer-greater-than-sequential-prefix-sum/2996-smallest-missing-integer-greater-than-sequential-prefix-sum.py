from typing import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        # Step 1: Calculate the longest sequential prefix sum starting at index 0
        ans = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                break
            ans += nums[i]
            
        # Step 2: Store elements in a set for O(1) membership lookup
        nums_set = set(nums)
        
        # Increment until we find the smallest integer not present in the array
        while ans in nums_set:
            ans += 1
            
        return ans

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna