from main import pair_document_with_format

def test():
    """Test the pair_document_with_format function."""
    
    # Test case 1: Basic filtering
    doc_names = ["report", "image", "data", "config"]
    doc_formats = ["pdf", "jpg", "csv", "json"]
    valid_formats = ["pdf", "csv"]
    
    result = pair_document_with_format(doc_names, doc_formats, valid_formats)
    expected = [("report", "pdf"), ("data", "csv")]
    
    print("🧪 TEST 1: Basic filtering")
    print(f"Input names: {doc_names}")
    print(f"Input formats: {doc_formats}")
    print(f"Valid formats: {valid_formats}")
    print(f"Result: {result}")
    print(f"Expected: {expected}")
    print(f"✅ PASS" if result == expected else f"❌ FAIL")
    print()
    
    # Test case 2: All formats valid
    valid_formats_all = ["pdf", "jpg", "csv", "json"]
    result2 = pair_document_with_format(doc_names, doc_formats, valid_formats_all)
    expected2 = [("report", "pdf"), ("image", "jpg"), ("data", "csv"), ("config", "json")]
    
    print("🧪 TEST 2: All formats valid")
    print(f"Valid formats: {valid_formats_all}")
    print(f"Result: {result2}")
    print(f"Expected: {expected2}")
    print(f"✅ PASS" if result2 == expected2 else f"❌ FAIL")
    print()
    
    # Test case 3: No valid formats
    valid_formats_none = ["txt", "docx"]
    result3 = pair_document_with_format(doc_names, doc_formats, valid_formats_none)
    expected3 = []
    
    print("🧪 TEST 3: No valid formats")
    print(f"Valid formats: {valid_formats_none}")
    print(f"Result: {result3}")
    print(f"Expected: {expected3}")
    print(f"✅ PASS" if result3 == expected3 else f"❌ FAIL")
    print()
    
    # Test case 4: Empty lists
    result4 = pair_document_with_format([], [], ["pdf"])
    expected4 = []
    
    print("🧪 TEST 4: Empty lists")
    print(f"Result: {result4}")
    print(f"Expected: {expected4}")
    print(f"✅ PASS" if result4 == expected4 else f"❌ FAIL")
    print()


def main():
    """Run all tests."""
    print("=" * 50)
    print("🔗 ZIP FUNCTION TESTS")
    print("=" * 50)
    test()
    print("🎯 Implement pair_document_with_format() to pass all tests!")


if __name__ == "__main__":
    main()