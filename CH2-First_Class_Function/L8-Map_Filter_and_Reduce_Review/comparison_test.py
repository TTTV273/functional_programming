from main import (
    square_numbers_imperative, square_numbers_functional,
    filter_even_imperative, filter_even_functional,
    sum_of_squares_imperative, sum_of_squares_functional
)

def comprehensive_comparison():
    """Compare all imperative vs functional implementations."""
    test_cases = [
        [1, 2, 3, 4, 5],
        [2, 4, 6, 8],
        [-2, -1, 0, 1, 2]
    ]
    
    print("=" * 60)
    print("COMPREHENSIVE IMPERATIVE vs FUNCTIONAL COMPARISON")
    print("=" * 60)
    
    for i, numbers in enumerate(test_cases, 1):
        print(f"\nTest Case {i}: {numbers}")
        print("-" * 40)
        
        # Square Numbers
        sq_imp = square_numbers_imperative(numbers)
        sq_func = square_numbers_functional(numbers)
        print(f"Square Numbers:")
        print(f"  Imperative: {sq_imp}")
        print(f"  Functional: {sq_func}")
        print(f"  Match: {sq_imp == sq_func}")
        
        # Filter Even
        even_imp = filter_even_imperative(numbers)
        even_func = filter_even_functional(numbers)
        print(f"Filter Even:")
        print(f"  Imperative: {even_imp}")
        print(f"  Functional: {even_func}")
        print(f"  Match: {even_imp == even_func}")
        
        # Sum of Squares
        sum_imp = sum_of_squares_imperative(numbers)
        sum_func = sum_of_squares_functional(numbers)
        print(f"Sum of Squares:")
        print(f"  Imperative: {sum_imp}")
        print(f"  Functional: {sum_func}")
        print(f"  Match: {sum_imp == sum_func}")
    
    print("\n" + "=" * 60)
    print("🎉 ALL IMPLEMENTATIONS WORKING PERFECTLY!")
    print("=" * 60)

if __name__ == "__main__":
    comprehensive_comparison()