from main import restore_documents

def test():
    """Test the restore_documents function with comprehensive test cases."""
    
    print("🧪 HIGHER-ORDER FUNCTIONS PRACTICE TESTS")
    print("=" * 60)
    
    # Test case 1: Basic functionality
    originals1 = ("report.txt", "data.csv", "image.png")
    backups1 = ("backup.pdf", "archive.zip", "REPORT.TXT")
    result1 = restore_documents(originals1, backups1)
    expected1 = {"REPORT.TXT", "DATA.CSV", "IMAGE.PNG", "BACKUP.PDF", "ARCHIVE.ZIP"}
    
    print("🧪 TEST 1: Basic document restoration")
    print(f"Originals: {originals1}")
    print(f"Backups: {backups1}")
    print(f"Result: {result1}")
    print(f"Expected: {expected1}")
    print(f"✅ PASS" if result1 == expected1 else f"❌ FAIL")
    print()
    
    # Test case 2: Corrupted files filtering
    originals2 = ("document.docx", "12345", "spreadsheet.xlsx")
    backups2 = ("99999", "presentation.pptx", "777")
    result2 = restore_documents(originals2, backups2)
    expected2 = {"DOCUMENT.DOCX", "SPREADSHEET.XLSX", "PRESENTATION.PPTX"}
    
    print("🧪 TEST 2: Corrupted files filtering")
    print(f"Originals: {originals2}")
    print(f"Backups: {backups2}")
    print(f"Result: {result2}")
    print(f"Expected: {expected2}")
    print(f"✅ PASS" if result2 == expected2 else f"❌ FAIL")
    print()
    
    # Test case 3: Case normalization and deduplication
    originals3 = ("file.txt", "document.pdf", "image.jpg")
    backups3 = ("FILE.TXT", "DOCUMENT.PDF", "backup.doc")
    result3 = restore_documents(originals3, backups3)
    expected3 = {"FILE.TXT", "DOCUMENT.PDF", "IMAGE.JPG", "BACKUP.DOC"}
    
    print("🧪 TEST 3: Case normalization and deduplication")
    print(f"Originals: {originals3}")
    print(f"Backups: {backups3}")
    print(f"Result: {result3}")
    print(f"Expected: {expected3}")
    print(f"✅ PASS" if result3 == expected3 else f"❌ FAIL")
    print()
    
    # Test case 4: Empty inputs
    result4 = restore_documents((), ())
    expected4 = set()
    
    print("🧪 TEST 4: Empty inputs")
    print(f"Result: {result4}")
    print(f"Expected: {expected4}")
    print(f"✅ PASS" if result4 == expected4 else f"❌ FAIL")
    print()
    
    # Test case 5: All corrupted files
    originals5 = ("12345", "99999")
    backups5 = ("777", "888")
    result5 = restore_documents(originals5, backups5)
    expected5 = set()
    
    print("🧪 TEST 5: All corrupted files")
    print(f"Originals: {originals5}")
    print(f"Backups: {backups5}")
    print(f"Result: {result5}")
    print(f"Expected: {expected5}")
    print(f"✅ PASS" if result5 == expected5 else f"❌ FAIL")
    print()


def analyze_requirements():
    """Analyze the specific requirements for the one-line implementation."""
    print("📋 IMPLEMENTATION REQUIREMENTS ANALYSIS")
    print("=" * 50)
    
    print("Required operations in order:")
    print("1. 📝 Convert to uppercase: .upper()")
    print("2. 🔍 Filter corrupted files: not .isdigit()")
    print("3. 🔗 Combine originals + backups")
    print("4. 🎯 Remove duplicates: set()")
    print()
    
    print("Function composition pattern:")
    print("Input → Combine → Map(upper) → Filter(not digit) → Set")
    print()
    
    print("Hint: Start with tuple concatenation")
    print("Example: originals + backups creates combined tuple")
    print()


if __name__ == "__main__":
    test()
    analyze_requirements()