class Solution:
        def findMax(self, n, a, b, k):
            # Create a difference array of size n + 1 initialized with 0
            diff = [0] * (n + 1)

            # Apply the range update queries
            m = len(a)
            for i in range(m):
                diff[a[i]] += k[i]
                diff[b[i] + 1] -= k[i]

            # Compute the prefix sum to reconstruct the array and track the maximum value
            max_val = 0
            current_sum = 0
            for i in range(n):
                current_sum += diff[i]
                if current_sum > max_val:
                    max_val = current_sum

            return max_val

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna