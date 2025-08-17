from main import *

run_cases = [
    (
        "* Star Wars episode 1 is underrated\n- Star Wars episode 9 is fine\n* Star Wars episode 3 is the best\n\n",
        "* Star Wars episode 1 is underrated\n* Star Wars episode 3 is the best\n\n",
    ),
    (
        "* Good line\n- Bad line to remove\n* Another good line\n",
        "* Good line\n* Another good line\n",
    ),
]

submit_cases = run_cases + [
    (
        "- Remove this line\n- And this one too\n* Keep this line\n* And this one\n- But not this\n",
        "* Keep this line\n* And this one\n",
    ),
    (
        "* First good line\n- First bad line\n* Second good line\n- Second bad line\n* Third good line\n\n",
        "* First good line\n* Second good line\n* Third good line\n\n",
    ),
]


def test(input_document, expected_output):
    print("---------------------------------")
    print("Input document:")
    print('"' + input_document + '"')
    print("Expected output:")
    print('"' + expected_output + '"')
    result = remove_invalid_lines(input_document)
    print("Actual output:")
    print('"' + str(result) + '"')
    if result == expected_output:
        print("Pass")
        return True

    if expected_output.endswith("\n") and not str(result).endswith("\n"):
        print("Fail")
        print("Reason: expected newline at the end of the output")
        return False

    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
