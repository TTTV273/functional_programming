import functools
from typing import Dict, List, Tuple

# ==================== ADVANCED FUNCTIONAL PROGRAMMING ====================
# Building on your map-filter-reduce mastery with real-world applications

# Sample data: Real estate contracts (matching your business!)
contracts = [
    {
        "id": 1,
        "type": "rental",
        "monthly_rent": 30_000_000,
        "duration": 60,
        "status": "active",
    },
    {
        "id": 2,
        "type": "rental",
        "monthly_rent": 25_000_000,
        "duration": 36,
        "status": "active",
    },
    {
        "id": 3,
        "type": "sale",
        "price": 15_000_000_000,
        "area": 200,
        "status": "pending",
    },
    {
        "id": 4,
        "type": "rental",
        "monthly_rent": 45_000_000,
        "duration": 24,
        "status": "expired",
    },
    {"id": 5, "type": "sale", "price": 8_000_000_000, "area": 120, "status": "active"},
    {
        "id": 6,
        "type": "rental",
        "monthly_rent": 60_000_000,
        "duration": 12,
        "status": "active",
    },
]

# ==================== CHALLENGE 1: FUNCTION COMPOSITION ====================


def calculate_total_rental_revenue(contracts_data):
    """
    Calculate total revenue from all ACTIVE rental contracts.
    Use functional programming: filter -> map -> reduce

    Expected result: 810,000,000 VND (monthly total from active rentals)
    """
    # TODO(human) - Implement using function composition
    # Step 1: Filter only active rental contracts
    # lambda c: c["type"] == "rental" and c["status"] == "active"
    active_rentals = filter(
        lambda c: c["type"] == "rental" and c["status"] == "active", contracts_data
    )
    # print(active_rentals)
    # Step 2: Map to extract monthly_rent values
    monthly_rent = map(lambda c: c["monthly_rent"], active_rentals)
    # Step 3: Reduce to sum the rents
    # Use one-liner function composition if possible!
    return functools.reduce(lambda a, b: a + b, monthly_rent)


def get_high_value_sales(contracts_data, min_price=10_000_000_000):
    """
    Get list of sale contracts above minimum price.
    Return list of contract IDs.

    Expected result: [3] (only contract 3 has price >= 10B)
    """
    # TODO(human) - Implement using filter + map
    # Filter sales above min_price, then map to extract IDs
    high_value_sales = filter(
        lambda c: c["type"] == "sale" and c["price"] >= min_price, contracts_data
    )
    sale_ids = map(lambda c: c["id"], high_value_sales)
    return list(sale_ids)


# ==================== CHALLENGE 2: DATA TRANSFORMATION PIPELINE ====================


def create_contract_summary(contracts_data):
    """
    Create summary statistics using functional programming.
    Return dict with multiple metrics calculated functionally.

    Expected result: {
        'total_contracts': 6,
        'active_rentals': 3,
        'average_rental_price': 45000000.0,
        'contract_types': {'rental': 4, 'sale': 2}
    }
    """
    # TODO(human) - Implement each metric using functional programming
    # Use combinations of map, filter, reduce for different calculations
    total_contracts = len(contracts_data)
    active_rentals = len(
        list(
            filter(
                lambda c: c["type"] == "rental" and c["status"] == "active",
                contracts_data,
            )
        )
    )
    all_rentals = filter(
        lambda c: c["type"] == "rental" and c["status"] == "active", contracts_data
    )
    rental_prices = list(map(lambda c: c["monthly_rent"], all_rentals))
    average_rental_price = sum(rental_prices) / len(rental_prices)
    contracts_types = functools.reduce(count_by_type_function, contracts_data, {})
    return {
        "total_contracts": total_contracts,
        "active_rentals": active_rentals,
        "average_rental_price": average_rental_price,
        "contracts_types": contracts_types,
    }


def count_by_type_function(current_dict, next_contract):
    contract_type = next_contract["type"]
    if contract_type in current_dict:
        current_dict[contract_type] += 1
    else:
        current_dict[contract_type] = 1
    return current_dict


# ==================== CHALLENGE 3: ADVANCED REDUCE PATTERNS ====================


def group_contracts_by_type(contracts_data):
    """
    Group contracts by type using reduce.
    Return dict: {'rental': [rental_contracts], 'sale': [sale_contracts]}

    This is advanced reduce - building dictionary structure!
    """
    # TODO(human) - Implement using functools.reduce
    # Start with empty dict, accumulate contracts into groups
    # Hint: Check if contract['type'] exists as key, create/append accordingly
    return functools.reduce(group_by_type_function, contracts_data, {})


def group_by_type_function(current_dict, next_contract):
    contract_type = next_contract["type"]

    if contract_type in current_dict:
        current_dict[contract_type].append(next_contract)
    else:
        current_dict[contract_type] = [next_contract]

    return current_dict


def find_best_contract(contracts_data):
    """
    Find highest value contract using reduce.
    For rentals: monthly_rent * duration
    For sales: price
    Return the contract dict with highest total value.
    """
    # TODO(human) - Implement using functools.reduce
    # Need helper function to calculate contract value
    # Then reduce to find maximum value contract
    return functools.reduce(compare_contracts, contracts_data)


def compare_contracts(best_so_far, next_contract):
    best_value = contract_total_value(best_so_far)
    next_value = contract_total_value(next_contract)

    if next_value > best_value:
        return next_contract
    else:
        return best_so_far


# ==================== HELPER FUNCTIONS ====================


def contract_total_value(contract):
    """Calculate total value of a contract."""
    if contract["type"] == "rental":
        return contract["monthly_rent"] * contract["duration"]
    else:  # sale
        return contract["price"]


# ==================== DEMO FUNCTIONS ====================


def demonstrate_functional_power():
    """Show the power of functional programming with real data."""
    print("🏢 REAL ESTATE CONTRACT ANALYSIS")
    print("=" * 50)

    print(f"📋 Total contracts: {len(contracts)}")
    print(f"💰 Sample contract values:")
    for contract in contracts[:3]:
        value = contract_total_value(contract)
        print(f"   Contract {contract['id']}: {value:,} VND")

    print("\n🎯 Ready for functional programming challenges!")
    print("Implement the functions above to analyze this data functionally!")


if __name__ == "__main__":
    demonstrate_functional_power()
