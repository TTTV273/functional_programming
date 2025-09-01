def word_count_aggregator():
    # TODO: Step 1 - Initialize the enclosed variable that will keep track of total word count
    # Hint: This should start at 0 and will store the running total
    count = 0

    # TODO: Step 2 - Define the inner function that will be returned
    # This function should:
    # - Take one parameter (doc) which is a string
    # - Count words in the doc string using .split()
    # - Add that count to the enclosed variable (remember nonlocal!)
    # - Return the new total
    def count_total(word):
        nonlocal count
        count += len(word.split())
        return count

    # TODO: Step 3 - Return the inner function (not called, just the function itself)
    return count_total
