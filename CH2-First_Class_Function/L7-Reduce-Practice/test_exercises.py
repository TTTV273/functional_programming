from practice_exercises import *

# Test cases for all 5 exercises
test_cases = {
    "sum_numbers": [
        ([1, 2, 3, 4], 10),
        ([5, 10, 15], 30),
        ([100], 100),
        ([-1, -2, -3], -6),
        ([1, -1, 2, -2], 0),
    ],
    
    "find_maximum": [
        ([3, 7, 2, 9, 1], 9),
        ([1, 1, 1], 1),
        ([100], 100),
        ([-5, -1, -10], -1),
        ([0, -5, 3, -2], 3),
    ],
    
    "count_words": [
        (["apple", "banana", "apple"], {"apple": 2, "banana": 1}),
        (["cat", "dog", "cat", "bird", "dog", "cat"], {"cat": 3, "dog": 2, "bird": 1}),
        (["hello"], {"hello": 1}),
        (["test", "test", "test"], {"test": 3}),
        (["a", "b", "c", "a", "b", "a"], {"a": 3, "b": 2, "c": 1}),
    ],
    
    "flatten_lists": [
        ([[1, 2], [3, 4], [5]], [1, 2, 3, 4, 5]),
        ([[1], [2], [3]], [1, 2, 3]),
        ([["a", "b"], ["c"]], ["a", "b", "c"]),
        ([[]], []),
        ([[1, 2, 3], [4, 5, 6, 7]], [1, 2, 3, 4, 5, 6, 7]),
    ],
    
    "build_url": [
        (["https://api.example.com", "users", "123", "posts"], "https://api.example.com/users/123/posts"),
        (["http://site.com/", "api", "data"], "http://site.com/api/data"), 
        (["https://example.com"], "https://example.com"),
        (["base", "path1", "path2"], "base/path1/path2"),
        (["http://api.com/v1/", "users/", "profile"], "http://api.com/v1/users/profile"),
    ],
}


def test_function(func_name, test_cases_list):
    """Test a specific function with its test cases."""
    print(f"\n{'='*50}")
    print(f"Testing {func_name}")
    print(f"{'='*50}")
    
    function = globals()[func_name]
    passed = 0
    failed = 0
    
    for i, (input_data, expected) in enumerate(test_cases_list, 1):
        print(f"\nTest {i}:")
        print(f"Input: {input_data}")
        print(f"Expected: {expected}")
        
        try:
            result = function(input_data)
            print(f"Got: {result}")
            
            if result == expected:
                print("✅ PASS")
                passed += 1
            else:
                print("❌ FAIL")
                failed += 1
                
        except Exception as e:
            print(f"❌ ERROR: {e}")
            failed += 1
    
    print(f"\n{func_name} Results: {passed} passed, {failed} failed")
    return passed, failed


def run_all_tests():
    """Run all exercise tests."""
    print("🧪 Reduce Practice Exercises - Test Suite")
    print("Bộ kiểm tra bài tập luyện tập Reduce")
    
    total_passed = 0
    total_failed = 0
    
    for func_name, cases in test_cases.items():
        passed, failed = test_function(func_name, cases)
        total_passed += passed
        total_failed += failed
    
    print(f"\n{'='*60}")
    print(f"FINAL RESULTS / KẾT QUẢ CUỐI CÙNG")
    print(f"{'='*60}")
    print(f"Total Tests: {total_passed + total_failed}")
    print(f"✅ Passed: {total_passed}")
    print(f"❌ Failed: {total_failed}")
    
    if total_failed == 0:
        print("🎉 ALL TESTS PASSED! / TẤT CẢ BÀI KIỂM TRA ĐỀU THÀNH CÔNG!")
        print("You've mastered the reduce function! / Bạn đã thành thạo hàm reduce!")
    else:
        print(f"Keep practicing! / Tiếp tục luyện tập!")


def test_individual(exercise_number):
    """Test a specific exercise by number (1-5)."""
    exercise_names = ["sum_numbers", "find_maximum", "count_words", "flatten_lists", "build_url"]
    
    if 1 <= exercise_number <= 5:
        func_name = exercise_names[exercise_number - 1]
        test_function(func_name, test_cases[func_name])
    else:
        print("Please enter a number between 1 and 5")


if __name__ == "__main__":
    # Run all tests by default
    run_all_tests()
    
    # To test individual exercises, uncomment one of these:
    # test_individual(1)  # Test sum_numbers
    # test_individual(2)  # Test find_maximum  
    # test_individual(3)  # Test count_words
    # test_individual(4)  # Test flatten_lists
    # test_individual(5)  # Test build_url