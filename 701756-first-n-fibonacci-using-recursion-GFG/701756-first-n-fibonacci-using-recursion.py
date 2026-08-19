class Solution:
    #Function to return list containing first n fibonacci numbers.
    def fibonacciNumbers(self,n):
            # Base case for n = 1
            if n == 1:
                return [0]

            # Base case for n = 2
            if n == 2:
                return [0, 1]

            # Recursively get the first n-1 Fibonacci numbers
            fib_list = self.fibonacciNumbers(n - 1)

            # Append the sum of the last two elements to get the next term
            fib_list.append(fib_list[-1] + fib_list[-2])

            return fib_list

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna