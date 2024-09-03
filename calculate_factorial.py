def calculate_factorial(n):
    if n == 0 or n == 1:
        return 1
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
    return factorial

result = calculate_factorial(7)
print(result)  # Output will be 5040 (since 7! = 7 *6 * 5 * 4 * 3 * 2 * 1)

result = calculate_factorial(0)
print(result)  # Output will be 1 (since 0! = 1)
