def pair_document_with_format(doc_names, doc_formats, valid_formats):
    """
    Pair document names with their formats and filter by valid formats.

    Args:
        doc_names: List of document names (strings)
        doc_formats: List of document formats (strings)
        valid_formats: List of valid format strings to filter by

    Returns:
        List of tuples where each tuple contains (doc_name, doc_format)
        and the format is in valid_formats

    Example:
        doc_names = ["report", "image", "data"]
        doc_formats = ["pdf", "jpg", "csv"]
        valid_formats = ["pdf", "csv"]
        Result: [("report", "pdf"), ("data", "csv")]
    """
    # TODO(human) - Implement this function using zip and filter
    # Step 1: Use zip() to pair doc_names with doc_formats
    doc_pairs = list(zip(doc_names, doc_formats))
    # Step 2: Use filter() to keep only tuples where format is in valid_formats
    # Step 3: Convert to list and return
    return list(filter(lambda c: c[1] in valid_formats, doc_pairs))


# Demo function to show zip in action
def demonstrate_zip():
    """Show basic zip functionality with examples."""
    print("🔗 ZIP FUNCTION DEMONSTRATION")
    print("=" * 40)

    # Basic zip example
    numbers = [1, 2, 3]
    letters = ["a", "b", "c"]
    paired = list(zip(numbers, letters))
    print(f"Numbers: {numbers}")
    print(f"Letters: {letters}")
    print(f"Zipped: {paired}")
    print()

    # Document example
    doc_names = ["report", "image", "data", "config"]
    doc_formats = ["pdf", "jpg", "csv", "json"]
    doc_pairs = list(zip(doc_names, doc_formats))
    print(f"Document names: {doc_names}")
    print(f"Document formats: {doc_formats}")
    print(f"Paired documents: {doc_pairs}")
    print()

    # Length mismatch example
    short_list = [1, 2]
    long_list = ["a", "b", "c", "d"]
    mismatched = list(zip(short_list, long_list))
    print(f"Short: {short_list}")
    print(f"Long: {long_list}")
    print(f"Zip result: {mismatched}")
    print("Note: Zip stops at shortest list length!")


if __name__ == "__main__":
    demonstrate_zip()

