# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a functional programming exercise repository focused on Python implementations. The project is structured as numbered exercises (01, 02, 04, 05, 07, etc.) and chapter-based lessons (CH2-First_Class_Function/) where each directory contains:

- `main.py` - The primary implementation file with the exercise solution
- `main_test.py` - Test suite with predefined test cases and custom testing framework
- `Lesson.md` - Educational content and exercise instructions (in lesson directories)

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

## Key Functional Programming Concepts

### Function Composition (Exercise 01)
- Pattern: `stylize_title(document)` calls `add_border(center_title(document))`
- Break complex chains into readable intermediate steps
- Use descriptive function names for clarity

### Debugging Techniques (Exercise 05)
Based on completed debugging exercise:

#### Break Complex Chains
- Avoid unreadable one-liners like `f(g(h(x)))`
- Break into intermediate variables for each step
- Use descriptive variable names (e.g., `stripped`, `capitalized`, `no_periods`)

#### Strategic Print Debugging
- Add print statements between transformation steps
- Use `print(f"|{variable}|")` to visualize hidden whitespace
- Remove debug prints after bugs are fixed, keep readable structure

#### Incremental Development
- Fix and test one step at a time
- Verify each transformation works before proceeding

### Advanced Validation Patterns (Exercise 07)
Based on completed hex-to-RGB exercise:

#### Two-Stage Validation Pattern
- **Stage 1**: Check type safety before operations that could crash
- **Stage 2**: Validate content only after type is confirmed
- Example: Check `isinstance(input, str)` before calling `len(input)`

#### Type Safety in Input Validation
- Operations like `len()`, string slicing can crash on wrong types
- Always validate input type before performing type-specific operations
- Separate checks prevent wrong exception types and messages

#### Number Base Conversion Debugging
- Common bug: `int(hex_string, 10)` vs `int(hex_string, 16)`
- Use strategic print debugging to identify base parameter errors
- String slicing patterns: `hex_color[0:2]`, `hex_color[2:4]`, `hex_color[4:6]`

### First-Class Functions (CH2-L1)
Based on completed Functions As Values lesson:

#### Functions As Values Concept
- Functions are first-class citizens in Python - can be assigned, passed, returned
- Example: `my_func = some_function` (assigns function, doesn't call it)
- Core principle: Functions can be treated like any other data type

#### Higher-Order Functions
- Functions that take other functions as parameters
- Example: `file_to_prompt(file, to_string)` - `to_string` is passed as parameter
- Enables separation of concerns and composability

#### Practical Implementation Patterns
- **Function composition**: `result = f(g(h(x)))` becomes modular
- **Strategy pattern**: Different functions for different processing needs
- **Callback pattern**: Pass functions to handle specific behaviors

#### String Formatting and Escape Characters
- Use `\n` for newlines in formatted strings
- Pattern: `f"```\n{content}\n```"` for markdown code blocks
- Clean two-line implementations: capture result, then format and return

### Anonymous Functions (CH2-L2)
Based on completed Lambda Functions lesson:

#### Lambda Functions Concept
- Anonymous functions with no name: `lambda x: x + 1`
- Automatic return - no `return` statement needed
- Used for small, simple evaluations and inline function definitions
- Can be assigned to variables like any other value

#### Tuple Unpacking in Loops
- Pattern: `for file_type, extensions in file_extension_tuples:`
- Automatically "unpacks" tuple elements into separate variables
- More readable than accessing via indices (`item[0]`, `item[1]`)
- Essential for processing structured data in functional programming

#### Closures and Function Factories
- **Factory Pattern**: Functions that create and return other functions
- **Closure**: Returned lambda functions "remember" variables from parent scope
- **Mental Model**: Factory builds "brain" (data), creates "robot" (lambda) with "backpack" (closure)
- Example: `file_type_getter` builds extension_map, returns lambda that uses it

#### Code Separation Principles
- Separate data building from function creation for clarity
- Pattern: `build_extension_map()` + `create_file_checker()` vs combined approach
- Each function has single responsibility: build data OR create function
- Improves reusability and testing

#### Dictionary Building from Nested Structures
- Transform nested tuples into flat lookup dictionaries
- Pattern: `[("type", [".ext1", ".ext2"])]` → `{".ext1": "type", ".ext2": "type"}`
- Use nested loops with tuple unpacking for clean iteration
- Safe lookups with `.get(key, default)` for missing keys

## Project Structure Notes

- Repository contains mix of completed exercises (01, 04, 05, 07, CH2-L1) and lesson materials
- Some directories (06, CH2-L2) contain only lesson content without implementations
- `Lecture.md` provides Vietnamese language context on Python's limitations for functional programming
- `learnlua.lua` file present but not part of main exercise structure