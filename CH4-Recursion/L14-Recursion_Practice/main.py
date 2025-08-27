def find_longest_word(document, longest_word=""):
    """
    Find the longest word in a document using pure recursion (no loops).

    Args:
        document: String containing text to search
        longest_word: Current longest word found so far (accumulator)

    Returns:
        String representing the longest word in the document
    """

    # Step 1: BASE CASE - When to stop recursion?
    # TODO: Check if document is empty or only whitespace
    # If so, return the current longest_word
    # Hint: document.strip() removes whitespace, check if result is empty
    if not document.strip():
        return longest_word

    # Step 2: SPLIT THE DOCUMENT - Get first word and remainder
    # TODO: Use document.split(maxsplit=1) to get [first_word, rest_of_string]
    # This gives you the first word to process and the rest to recurse on
    parts = document.split(maxsplit=1)

    # Step 3: EXTRACT PARTS - Handle the split result safely
    # TODO: Get the first_word from the split result (parts[0])
    # TODO: Check if there's a remainder (len(parts) > 1), if so get parts[1]
    first_word = parts[0]
    rest_of_string = ""
    if len(parts) > 1:
        rest_of_string = parts[1]

    # Step 4: COMPARE LENGTHS - Decide which word is longer
    # TODO: Compare len(first_word) with len(longest_word)
    # Only update if first_word is LONGER (not equal) than longest_word
    if len(first_word) > len(longest_word):
        longest_word = first_word

    # Step 5: RECURSIVE CALL - Process the remainder of the document
    # TODO: If there's remainder text, recursively call find_longest_word()
    # Pass the remainder and the current best longest_word
    # TODO: If no remainder, return the longest_word (this is also a base case)
    if rest_of_string:
        return find_longest_word(rest_of_string, longest_word)
    return longest_word
    # Remember: This follows your L4-Zipmap pattern:
    # L4: Process first key/value, recurse on remaining lists
    # L14: Process first word, recurse on remaining document
