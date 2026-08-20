class Solution:
    def maxSumWithK(self, arr: list[int], k: int) -> int:
        
            n = len(arr)

            # Calculate the sum of the first k elements
            curr_sum = sum(arr[:k])
            max_sum = curr_sum

            running_prefix = 0

            # Slide the window from index k to n - 1
            for i in range(k, n):
                curr_sum += arr[i]
                running_prefix += arr[i - k]

                # If the prefix elements sum up to a negative value, 
                # discarding them increases the overall subarray sum.
                if running_prefix < 0:
                    curr_sum -= running_prefix
                    running_prefix = 0

                max_sum = max(max_sum, curr_sum)

            return max_sum

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna