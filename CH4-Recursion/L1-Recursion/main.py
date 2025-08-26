def factorial_r(x):
    # TODO(human): Implement the recursive factorial logic here
    # Hints from lesson:
    # 1. Base case: What should factorial_r(0) return? (hint: 0! = 1)
    if x == 0:
        return 1
    # 2. Recursive case: How do you break n! into n * (something smaller)?
    # 3. Remember: n! = n × (n-1) × (n-2) × ... × 1
    return x * factorial_r(x - 1)
