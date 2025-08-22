from advanced_functional import (
    contracts, 
    calculate_total_rental_revenue,
    get_high_value_sales,
    create_contract_summary,
    group_contracts_by_type,
    find_best_contract
)

def test_all_functions():
    """Test all advanced functional programming implementations."""
    print("🧪 TESTING ADVANCED FUNCTIONAL PROGRAMMING")
    print("=" * 60)
    
    # Test 1: Total Rental Revenue
    print("\n1️⃣ Total Active Rental Revenue:")
    try:
        revenue = calculate_total_rental_revenue(contracts)
        expected = 135_000_000  # 30M + 25M + 45M + 60M from active rentals
        print(f"   Result: {revenue:,} VND")
        print(f"   Expected: {expected:,} VND")
        print(f"   ✅ PASS" if revenue == expected else f"   ❌ FAIL")
    except Exception as e:
        print(f"   ❌ ERROR: {e}")
    
    # Test 2: High Value Sales
    print("\n2️⃣ High Value Sales (>= 10B):")
    try:
        high_sales = get_high_value_sales(contracts)
        expected = [3]
        print(f"   Result: {high_sales}")
        print(f"   Expected: {expected}")
        print(f"   ✅ PASS" if high_sales == expected else f"   ❌ FAIL")
    except Exception as e:
        print(f"   ❌ ERROR: {e}")
    
    # Test 3: Contract Summary
    print("\n3️⃣ Contract Summary:")
    try:
        summary = create_contract_summary(contracts)
        print(f"   Result: {summary}")
        # Expected calculations shown for reference
        print(f"   Expected total_contracts: 6")
        print(f"   Expected active_rentals: 3") 
        print(f"   Expected average_rental_price: 40,000,000")
    except Exception as e:
        print(f"   ❌ ERROR: {e}")
    
    # Test 4: Group by Type
    print("\n4️⃣ Group Contracts by Type:")
    try:
        grouped = group_contracts_by_type(contracts)
        print(f"   Rental contracts: {len(grouped.get('rental', []))}")
        print(f"   Sale contracts: {len(grouped.get('sale', []))}")
        print(f"   Expected: 4 rentals, 2 sales")
    except Exception as e:
        print(f"   ❌ ERROR: {e}")
    
    # Test 5: Best Contract
    print("\n5️⃣ Highest Value Contract:")
    try:
        best = find_best_contract(contracts)
        print(f"   Best contract ID: {best['id']}")
        print(f"   Type: {best['type']}")
        if best['type'] == 'rental':
            value = best['monthly_rent'] * best['duration']
        else:
            value = best['price']
        print(f"   Total value: {value:,} VND")
    except Exception as e:
        print(f"   ❌ ERROR: {e}")

if __name__ == "__main__":
    test_all_functions()