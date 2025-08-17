from main import *

# Test functions for apply_operation
def square(x):
    return x * x

def double(x):
    return x * 2

run_cases = [
    # Test apply_operation with square function
    (apply_operation, square, [1, 2, 3], [1, 4, 9]),
    # Test apply_operation with double function  
    (apply_operation, double, [1, 2, 3], [2, 4, 6]),
    # Test create_math_operation with square
    (create_math_operation, "square", 5, 25),
    # Test create_math_operation with double
    (create_math_operation, "double", 4, 8),
]

submit_cases = run_cases + [
    # Additional tests for apply_operation
    (apply_operation, square, [0, -2, 10], [0, 4, 100]),
    (apply_operation, double, [-1, 0, 5], [-2, 0, 10]),
    # Additional tests for create_math_operation
    (create_math_operation, "increment", 3, 4),
    (create_math_operation, "unknown", 5, None),
]

def test_apply_operation(func, operation, numbers, expected_output):
    print("---------------------------------")
    print(f"Testing: {func.__name__}")
    print(f"Operation: {operation.__name__}")
    print(f"Numbers: {numbers}")
    print(f"Expecting: {expected_output}")
    try:
        result = func(operation, numbers)
        print(f"Actual: {result}")
        if result == expected_output:
            print("Pass")
            return True
        print("Fail")
        return False
    except Exception as e:
        print("Fail")
        print(f"Error: {e}")
        return False

def test_create_math_operation(func, operation_type, test_input, expected_output):
    print("---------------------------------")
    print(f"Testing: {func.__name__}")
    print(f"Operation type: {operation_type}")
    print(f"Test input: {test_input}")
    print(f"Expecting: {expected_output}")
    try:
        operation_func = func(operation_type)
        if operation_func is None and expected_output is None:
            print("Actual: None")
            print("Pass")
            return True
        elif operation_func is None:
            print("Actual: None")
            print("Fail")
            return False
        else:
            result = operation_func(test_input)
            print(f"Actual: {result}")
            if result == expected_output:
                print("Pass")
                return True
            print("Fail")
            return False
    except Exception as e:
        print("Fail")
        print(f"Error: {e}")
        return False

def test(test_case):
    if len(test_case) == 4:
        # Check function type first to route correctly
        if test_case[0] == create_math_operation:
            func, operation_type, test_input, expected = test_case
            return test_create_math_operation(func, operation_type, test_input, expected)
        else:
            func, operation, numbers, expected = test_case
            return test_apply_operation(func, operation, numbers, expected)
    else:
        return False

def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")

test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()