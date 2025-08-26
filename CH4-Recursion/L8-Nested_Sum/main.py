def sum_nested_list(lst):
    # TODO(human): Implement the recursive nested list traversal logic here
    # Pseudocode from lesson:
    # 1. Create integer variable to track total size
    total = 0
    # 2. Loop through each item in the list:
    #    - If item is integer: add to total
    #    - If item is list: recursively call sum_nested_list, add result to total
    for item in lst:
        if isinstance(item, int):
            total += item
        elif isinstance(item, list):
            total += sum_nested_list(item)
    # 3. Return total size
    #
    # Hints:
    # - Use isinstance(item, list) to check if item is a list
    # - Use isinstance(item, int) to check if item is an integer
    # - This combines loops WITH recursion (different from previous patterns!)
    return total
