class Solution:
    def countMinOperations(self, arr):
            total_increments = 0
            max_doubles = 0

            for num in arr:
                current_doubles = 0
                while num > 0:
                    if num % 2 == 1:
                        total_increments += 1
                        num -= 1
                    else:
                        current_doubles += 1
                        num //= 2

                # The maximum doublings needed by any single element 
                # dictates the shared global doubling operations
                max_doubles = max(max_doubles, current_doubles)

            return total_increments + max_doubles

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna