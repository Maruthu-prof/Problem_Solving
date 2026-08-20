class Solution:
    def countPairs(self, arr: list[int], k: int) -> int:
            # Step 1: Sort the array to utilize the two-pointer strategy
            arr.sort()

            left = 0
            total_pairs = 0
            n = len(arr)

            # Step 2: Expand the window using the right pointer
            for right in range(n):
                # Shrink the window from the left if the condition is violated
                while arr[right] - arr[left] >= k:
                    left += 1

                # All elements from 'left' to 'right-1' form a valid pair with 'arr[right]'
                total_pairs += (right - left)

            return total_pairs

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna