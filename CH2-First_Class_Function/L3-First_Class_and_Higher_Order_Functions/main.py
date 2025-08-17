def square(x):
    return x * x


def double(x):
    return x * 2


def increment(x):
    return x + 1


def apply_operation(operation, numbers):
    # TODO(human) - Implement this higher-order function
    # This function should take a function (operation) and a list of numbers
    # Apply the operation function to each number in the list
    # Return a new list with the results
    # Example: apply_operation(square, [1, 2, 3]) should return [1, 4, 9]
    result = []
    for number in numbers:
        result.append(operation(number))
    return result


def create_math_operation(operation_type):
    # TODO(human) - Implement this function factory
    # This function should return different math functions based on operation_type
    # "square" -> return a function that squares numbers (x * x)
    # "double" -> return a function that doubles numbers (x * 2)
    # "increment" -> return a function that adds 1 to numbers (x + 1)
    # Use lambda functions for the returned operations
    # Return None for unknown operation types
    if operation_type == "square":
        # return square
        return lambda x: x * x
    elif operation_type == "double":
        # return double
        return lambda x: x * 2
    elif operation_type == "increment":
        # return increment
        return lambda x: x + 1
    else:
        return None

