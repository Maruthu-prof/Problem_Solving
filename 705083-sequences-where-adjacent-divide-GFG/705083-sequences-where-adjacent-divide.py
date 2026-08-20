class Solution:
        def count(self, n: int, m: int) -> int:
            # Dictionary to store the results of subproblems
            memo = {}

            def dfs(idx, last):
                # Base case: valid sequence found
                if idx == n:
                    return 1

                # Return cached result if already computed
                if (idx, last) in memo:
                    return memo[(idx, last)]

                total_sequences = 0

                # If it's the first element, try all numbers from 1 to m
                if idx == 0:
                    for v in range(1, m + 1):
                        total_sequences += dfs(idx + 1, v)
                else:
                    # For adjacent elements, check the divisibility condition
                    for v in range(1, m + 1):
                        if last % v == 0 or v % last == 0:
                            total_sequences += dfs(idx + 1, v)

                # Save to memoization table
                memo[(idx, last)] = total_sequences
                return total_sequences

            return dfs(0, 0)

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna