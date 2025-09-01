def formatter(pattern):
    """
    Function transformation that creates specialized text formatters.

    Args:
        pattern (str): Template with '{}' placeholder for text insertion

    Returns:
        function: Specialized formatter function that applies the pattern
    """

    # TODO(human): Implement the inner function that processes the pattern
    def inner_func(text):
        result = ""
        i = 0
        while i < len(pattern):
            if pattern[i : i + 2] == "{}":
                result += text
                i += 2
            else:
                result += pattern[i]
                i += 1
        return result

    return inner_func
    # Hint: Use a loop to scan through the pattern character by character
    # When you find '{}', replace it with the input text
    # Otherwise, copy the pattern character directly
    pass


def get_document_formatter(doc_type):
    """
    Creates specialized document formatters for Doc2Doc system.

    This demonstrates practical function transformation for Vietnamese business:
    - "heading" -> creates title formatters with === borders
    - "emphasis" -> creates bold/italic formatters
    - "list" -> creates bullet point formatters

    Args:
        doc_type (str): Type of document formatting needed

    Returns:
        function: Specialized formatter for that document type
    """
    # TODO(human): Implement document type selection
    # Use if/elif statements to return different formatter patterns:
    # - "heading": "=== {} ==="
    # - "emphasis": "**{}**"
    # - "list": "• {}"
    # - default: "{}" (no formatting)
    if doc_type == "heading":
        return formatter("=== {} ===")
    elif doc_type == "emphasis":
        return formatter("**{}**")
    elif doc_type == "list":
        return formatter("• {}")
    else:
        return formatter("{}")

