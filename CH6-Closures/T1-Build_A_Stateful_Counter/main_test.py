from main import make_counter, make_prefixer


def run_counter_case(case):
    start = case["start"]
    step = case["step"]
    steps = case["steps"]
    expected = case["expected"]

    n, r, p = make_counter(start, step)

    results = []
    for s in steps:
        if s == "peek":
            results.append(p())
        elif s == "next":
            results.append(n())
        elif isinstance(s, tuple) and s[0] == "reset":
            # s = ("reset", value_or_None)
            results.append(r(s[1]))
        else:
            raise ValueError(f"Unknown step: {s}")

    print("---------------------------------")
    print("Input:")
    print(f"  make_counter(start={start}, step={step})")
    print("  Steps:")
    for s in steps:
        if s == "peek" or s == "next":
            print(f"    - {s}()")
        else:
            print(f"    - reset({s[1]!r})")
    print("")
    print(f"Expected: {expected}")
    print(f"Actual:   {results}")

    if results == expected:
        print("Pass")
        return True
    print("Fail")
    return False


def run_prefixer_case(case):
    prefix = case["prefix"]
    inputs = case["inputs"]
    expected = case["expected"]

    f = make_prefixer(prefix)
    results = [f(x) for x in inputs]

    print("---------------------------------")
    print("Input:")
    print(f"  make_prefixer(prefix={prefix!r})")
    print(f"  Messages: {inputs}")
    print("")
    print(f"Expected: {expected}")
    print(f"Actual:   {results}")

    if results == expected:
        print("Pass")
        return True
    print("Fail")
    return False


counter_run_cases = [
    {
        "start": 10,
        "step": 5,
        "steps": ["peek", "next", "next", "peek", ("reset", None), "peek"],
        "expected": [10, 10, 15, 20, 10, 10],
    }
]

prefixer_run_cases = [
    {
        "prefix": "[INFO]",
        "inputs": ["Server started", "Listening on 8080"],
        "expected": ["[INFO] Server started", "[INFO] Listening on 8080"],
    }
]

counter_submit_cases = counter_run_cases + [
    {
        "start": -3,
        "step": -2,
        "steps": ["peek", "next", "next", "next", "peek"],
        "expected": [-3, -3, -5, -7, -9],
    },
    {
        "start": 0,
        "step": 3,
        "steps": ["next", "next", ("reset", 100), "peek", "next"],
        "expected": [0, 3, 100, 100, 100],
    },
]

prefixer_submit_cases = prefixer_run_cases + [
    {
        "prefix": "[DEBUG]",
        "inputs": ["x=1", "y=2"],
        "expected": ["[DEBUG] x=1", "[DEBUG] y=2"],
    },
    {
        "prefix": "(user)",
        "inputs": ["alice", "bob"],
        "expected": ["(user) alice", "(user) bob"],
    },
]


# Additional independence test (counters and prefixers shouldn't interfere)


def independence_test():
    print("---------------------------------")
    print("Input: Independence check with two counters")
    c1n, c1r, c1p = make_counter(5, 2)
    c2n, c2r, c2p = make_counter(100, 10)

    seq = [c1p(), c1n(), c2p(), c2n(), c1n(), c2n(), c1p(), c2p()]
    expected = [5, 5, 100, 100, 7, 110, 9, 120]

    print(f"Expected: {expected}")
    print(f"Actual:   {seq}")
    if seq == expected:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    # choose run or submit sets
    cr = counter_submit_cases
    pr = prefixer_submit_cases
    if "__RUN__" in globals():
        cr = counter_run_cases
        pr = prefixer_run_cases

    passed = 0
    failed = 0

    print("Testing make_counter...")
    for case in cr:
        if run_counter_case(case):
            passed += 1
        else:
            failed += 1

    print("\nTesting make_prefixer...")
    for case in pr:
        if run_prefixer_case(case):
            passed += 1
        else:
            failed += 1

    print("\nTesting independence...")
    if independence_test():
        passed += 1
    else:
        failed += 1

    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    print(f"{passed} passed, {failed} failed")


main()
