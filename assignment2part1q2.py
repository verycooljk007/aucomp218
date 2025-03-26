def fibo(n):
    fl = []  # Initialize an empty list to store Fibonacci numbers.

    # Check if n is a non-negative integer.
    if not isinstance(n, int) or n < 0:
        return fl  # If n is not valid, return an empty list.

    fl = [1, 1]  # Initialize the Fibonacci sequence with the first two numbers.

    # Loop to generate Fibonacci numbers from index 2 to n.
    for i in range(2, n + 1):
        fl += [fl[i - 1] + fl[i - 2]]  # Append the sum of the previous two numbers.

    return fl  # Return the complete Fibonacci sequence.
print(fibo(5))  # Output should be [1, 1, 2, 3, 5, 8]
