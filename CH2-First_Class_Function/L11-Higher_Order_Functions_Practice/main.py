def restore_documents(originals, backups):
    """
    Restore documents by combining originals and backups, filtering corrupted files.

    Args:
        originals: Tuple of original document strings
        backups: Tuple of backup document strings

    Returns:
        Set of valid documents (uppercase, non-corrupted, deduplicated)

    Processing steps:
        1. Convert all documents to uppercase for consistency
        2. Filter out corrupted documents (those containing only digits)
        3. Combine originals and backups
        4. Remove duplicates using set

    Example:
        originals = ("Report.txt", "data.csv", "12345")
        backups = ("REPORT.TXT", "backup.pdf", "9999")
        Result: {"REPORT.TXT", "DATA.CSV", "BACKUP.PDF"}
    """
    # TODO(human) - Implement in one line using map, filter, and set operations
    # Hint: Combine tuples first, then map to uppercase, then filter non-digits, then set
    return set(
        filter(
            lambda doc: not doc.isdigit(),
            map(lambda doc: doc.upper(), originals + backups),
        )
    )


# Demo function to show the document restoration process
def demonstrate_document_restore():
    """Show document restoration with various test cases."""
    print("📁 DOCUMENT RESTORATION DEMONSTRATION")
    print("=" * 50)

    # Test case 1: Basic restoration
    originals1 = ("report.txt", "data.csv", "image.png")
    backups1 = ("REPORT.TXT", "backup.pdf", "archive.zip")
    print(f"Originals: {originals1}")
    print(f"Backups: {backups1}")
    print(f"Expected: Mix of original and backup files, uppercased, no duplicates")
    print()

    # Test case 2: With corrupted files
    originals2 = ("document.docx", "12345", "spreadsheet.xlsx")
    backups2 = ("99999", "DOCUMENT.DOCX", "presentation.pptx")
    print(f"Originals with corruption: {originals2}")
    print(f"Backups with corruption: {backups2}")
    print(f"Expected: Valid documents only, corrupted files (digits) removed")
    print()

    # Test case 3: Case sensitivity and duplicates
    originals3 = ("file.txt", "FILE.TXT", "document.pdf")
    backups3 = ("file.txt", "backup.doc", "DOCUMENT.PDF")
    print(f"Mixed case originals: {originals3}")
    print(f"Mixed case backups: {backups3}")
    print(f"Expected: Uppercase versions, duplicates removed")
    print()

    print("🎯 Implement restore_documents() to process these cases!")


def test_string_methods():
    """Demonstrate the string methods used in the exercise."""
    print("\n🔍 STRING METHODS DEMONSTRATION")
    print("=" * 40)

    # .upper() demonstration
    docs = ["report.txt", "DATA.csv", "Image.PNG"]
    print("Upper case conversion:")
    for doc in docs:
        print(f"  '{doc}' → '{doc.upper()}'")
    print()

    # .isdigit() demonstration
    files = ["document.txt", "12345", "file123", "99999", "backup.pdf"]
    print("Corruption detection (isdigit):")
    for file in files:
        is_corrupted = file.isdigit()
        status = "CORRUPTED" if is_corrupted else "VALID"
        print(f"  '{file}' → {status}")
    print()


if __name__ == "__main__":
    demonstrate_document_restore()
    test_string_methods()

