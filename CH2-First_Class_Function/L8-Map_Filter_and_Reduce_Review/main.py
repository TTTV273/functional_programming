import functools

# ==================== FACTORIAL EXAMPLES ====================
# Compare imperative vs functional approaches


def factorial_imperative(n):
    """
    Calculate factorial using imperative approach with loops and mutable state.
    Factorial of n = n! = n × (n-1) × (n-2) × ... × 1
    Example: factorial(5) = 5 × 4 × 3 × 2 × 1 = 120
    """
    # Imperative: step-by-step procedure with mutable state
    result = 1
    for i in range(1, n + 1):
        result *= i  # Mutation! Variable changes each iteration
    return result


def factorial_functional(n):
    """
    Calculate factorial using functional approach with reduce.
    Same mathematical result, but expressed as function composition.
    """
    # Functional: declare what we want, not how to get it
    return functools.reduce(lambda x, y: x * y, range(1, n + 1))


# ==================== EXERCISE: SQUARE NUMBERS ====================


def square_numbers_imperative(numbers):
    """
    Square each number using imperative approach.
    Example: square_numbers([2, 3, 4]) = [4, 9, 16]
    """
    # TODO(human) - Implement imperative version using a for loop
    # Create empty result list, loop through numbers, append squared values
    result = []
    for num in numbers:
        result.append(num**2)
    return result


def square_numbers_functional(numbers):
    """
    Square each number using functional approach.
    Same result as imperative, but no loops or mutable state.
    """
    # Functional: one-line transformation using map
    return list(map(lambda x: x**2, numbers))


# ==================== EXERCISE: FILTER EVEN NUMBERS ====================


def filter_even_imperative(numbers):
    """
    Filter even numbers using imperative approach.
    Example: filter_even([1, 2, 3, 4, 5]) = [2, 4]
    """
    # TODO(human) - Implement imperative version
    # Use for loop with if condition to check num % 2 == 0
    result = []
    for num in numbers:
        if num % 2 == 0:
            result.append(num)
    return result


def filter_even_functional(numbers):
    """
    Filter even numbers using functional approach.
    No explicit loops or conditions - filter handles the logic.
    """
    # Functional: declarative filtering
    return list(filter(lambda x: x % 2 == 0, numbers))


# ==================== EXERCISE: SUM OF SQUARES ====================


def sum_of_squares_imperative(numbers):
    """
    Calculate sum of squares using imperative approach.
    Example: sum_of_squares([2, 3, 4]) = 2² + 3² + 4² = 4 + 9 + 16 = 29
    """
    # TODO(human) - Implement imperative version
    # Initialize total = 0, loop through numbers, total += num ** 2
    total = 0
    for num in numbers:
        total += num**2
    return total


def sum_of_squares_functional(numbers):
    """
    Calculate sum of squares using functional approach.
    Combines map (transformation) and reduce (accumulation).
    """
    # Functional: function composition - map then reduce
    squares = map(lambda x: x**2, numbers)
    return functools.reduce(lambda x, y: x + y, squares, 0)


# ==================== DEMONSTRATION FUNCTIONS ====================


def demonstrate_factorial():
    """Show factorial calculation with both approaches."""
    n = 5
    print(f"Factorial of {n}:")
    print(f"  Imperative: {factorial_imperative(n)}")
    print(f"  Functional: {factorial_functional(n)}")
    print()


def demonstrate_completed():
    """Show completed functional examples working."""
    test_numbers = [1, 2, 3, 4, 5]

    print("Functional Programming Examples:")
    print(f"Numbers: {test_numbers}")
    print(f"Squared: {square_numbers_functional(test_numbers)}")
    print(f"Even only: {filter_even_functional(test_numbers)}")
    print(f"Sum of squares: {sum_of_squares_functional(test_numbers)}")
    print()


if __name__ == "__main__":
    demonstrate_factorial()
    demonstrate_completed()
    print("Ready for you to implement the imperative versions!")

