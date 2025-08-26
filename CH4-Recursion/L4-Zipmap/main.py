def zipmap(keys, values):
    # TODO(human): Implement the recursive zipmap logic here
    # Pseudocode from lesson:
    # 1. Base case: If either keys or values is empty, return empty dictionary
    if not keys or not values:
        return {}
    # 2. Recursive case: zipmap on all but first elements (keys[1:], values[1:])
    rest = zipmap(keys[1:], values[1:])
    # 3. Add first key-value pair to resulting dictionary
    rest[keys[0]] = values[0]
    # 4. Return the updated dictionary
    return rest
