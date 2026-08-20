class Solution:
    def countSubarray(self, arr: list[int], l: int, r: int) -> int:
            # Helper function to count all subarrays with sum <= limit
            def countLessThanOrEqual(limit: int) -> int:
                if limit < 0:
                    return 0

                count = 0
                current_sum = 0
                left = 0

                # Slide the right pointer over the array
                for right in range(len(arr)):
                    current_sum += arr[right]

                    # Shrink the window from the left if the sum exceeds the limit
                    while current_sum > limit and left <= right:
                        current_sum -= arr[left]
                        left += 1

                    # All subarrays ending at 'right' and starting from 'left' to 'right' are valid
                    count += (right - left + 1)

                return count

            # Subarrays in range [l, r] = (Subarrays <= r) - (Subarrays <= l - 1)
            return countLessThanOrEqual(r) - countLessThanOrEqual(l - 1)

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna