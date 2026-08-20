class Solution:
    def countFriendsPairings(self, n: int) -> int:
             # Base cases: for 1 friend there's 1 way, for 2 friends there are 2 ways
             if n <= 2:
                 return n

             # a represents f(i-2), b represents f(i-1)
             a, b = 1, 2

             # Iteratively calculate ways up to n
             for i in range(3, n + 1):
                 current = b + (i - 1) * a
                 a = b
                 b = current

             return b

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna