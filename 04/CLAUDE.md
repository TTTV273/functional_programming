# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a functional programming exercise repository focused on Python implementations. The project is structured as numbered exercises (01, 02, 04, etc.) where each directory contains:

- `main.py` - The primary implementation file with the exercise solution
- `main_test.py` - Test suite with predefined test cases and testing framework

## Testing Framework

Each exercise uses a custom testing framework with two test case sets:
- `run_cases` - Basic test cases for initial development
- `submit_cases` - Complete test cases including edge cases

### Running Tests

```bash
# Run full test suite (submit_cases)
python main_test.py

# Run basic test cases only
python -c "__RUN__ = True; exec(open('main_test.py').read())"
```

The test framework automatically:
- Validates function output against expected results
- Checks input immutability (ensures functions don't modify input parameters)
- Provides detailed pass/fail reporting

## Code Architecture

### Exercise Structure
- Each numbered directory represents a distinct functional programming exercise
- Functions should be pure (no side effects, don't modify inputs)
- Implementations focus on immutability and functional programming principles

### Test Pattern
The testing framework follows a consistent pattern:
- `test()` function handles individual test case execution
- `main()` orchestrates test running and result reporting
- Test cases are tuples of (input, expected_output)
- Global `__RUN__` variable switches between run_cases and submit_cases

## Development Workflow

1. Implement solution in `main.py`
2. Test with basic cases: `python -c "__RUN__ = True; exec(open('main_test.py').read())"`
3. Test with full suite: `python main_test.py`
4. Ensure all tests pass and inputs remain unmodified