class Solution:
   
    def countTriplets(self, arr: list[int], l: int, r: int) -> int:
            # Helper function to count triplets with sum <= val
            def countLessThanOrEqual(val):
                count = 0
                n = len(arr)
                for i in range(n - 2):
                    j = i + 1
                    k = n - 1
                    while j < k:
                        if arr[i] + arr[j] + arr[k] <= val:
                            count += (k - j)
                            j += 1
                        else:
                            k -= 1
                return count

            # Sort the array to use the two-pointer technique
            arr.sort()

            # Triplets in range [l, r] = (Triplets <= r) - (Triplets <= l - 1)
            return countLessThanOrEqual(r) - countLessThanOrEqual(l - 1)

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna