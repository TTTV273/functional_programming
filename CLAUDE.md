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

### First Class and Higher Order Functions (CH2-L3)
Based on completed lesson with full implementation and testing:

#### First-Class Functions Definition
- Functions treated like any other variable in Python
- Can be assigned to variables, passed as arguments, returned from functions
- Core principle: functions are values that can be manipulated like data
- Example: `f = square` assigns function without calling it

#### Higher-Order Functions Types
- **Parameter Type**: Functions that accept other functions as arguments
- **Return Type**: Functions that return other functions as results
- **Both Types**: Functions can both take and return functions
- Pattern enables composition and reusable transformation logic

#### Apply Operation Pattern
- Generic function that applies operation to each element in a list
- Implementation: `apply_operation(operation, numbers)` with loop and append
- Demonstrates function-as-parameter pattern
- Equivalent to Python's built-in `map()` but with explicit implementation

#### Function Factory Pattern
- Functions that create and return other functions based on parameters
- Dynamic function creation at runtime based on string inputs
- Pattern: `create_math_operation("square")` returns `lambda x: x * x`
- Enables configurable behavior and specialized function generation

#### Lambda vs Named Functions Trade-offs
- **Named Functions**: Clear names, reusable, memory efficient, debugger-friendly
- **Lambda Functions**: Self-contained, meets exercise requirements, fresh instances
- **Both Approaches**: Functionally equivalent, demonstrate same concepts
- **Choice Factors**: Exercise requirements, debugging needs, code organization

#### Function Composition Patterns
- Combining function factories with apply operations
- Example: `apply_operation(create_math_operation("square"), [1,2,3])`
- Demonstrates full higher-order function ecosystem
- Enables building complex operations from simple components

#### Test Framework Design Principles
- Proper routing logic for different test types
- Check specific criteria before general conditions
- Function type identification for correct test execution
- Error handling and edge case coverage in test design

### Map Function (CH2-L4)
Based on completed lesson with Python's built-in map function:

#### Built-in Map Function Concept
- Python's `map(function, iterable)` applies function to each element in sequence
- Returns iterator object (not list) for memory efficiency
- Equivalent to custom `apply_operation` but optimized and built-in
- Part of functional programming trilogy: map, filter, reduce

#### Split → Map → Join Pattern
- **Split**: Break string into components with `.split("\n")`
- **Map**: Apply transformation function to each component
- **Join**: Reassemble components with `.join()` method
- Essential pattern for string/text processing in functional style

#### Iterator vs List Handling
- `map()` returns iterator object that can be consumed once
- Use `list(map_object)` to convert to list when needed
- `join()` can work directly with iterators (memory efficient)
- Iterator exhaustion: second conversion returns empty result

#### String Processing Applications
- Line-by-line text transformations (bullet point conversion)
- Document format standardization and cleanup
- Batch text processing without manual loops
- Preserving document structure and formatting

#### Functional vs Imperative Comparison
- **Imperative**: Manual loops with accumulator variables
- **Functional**: Single expression with map and helper function
- **Benefits**: Cleaner code, separation of concerns, reusability
- **Pattern**: Transform logic separate from iteration mechanics

#### Memory Efficiency Patterns
- Map objects are lazy and memory-efficient
- Process large datasets without loading entire result into memory
- Chain multiple transformations using iterator composition
- Direct iterator usage with string operations like `join()`

### Filter Function (CH2-L6)
Based on completed lesson with Python's built-in filter function:

#### Built-in Filter Function Concept
- Python's `filter(predicate, iterable)` selects elements where predicate returns True
- Acts as "quality inspector" - only items passing the test get through
- Returns iterator object for memory efficiency
- Core functional programming tool alongside map and reduce

#### Split → Filter → Join Pattern
- **Split**: Break string into components with `.split("\n")`
- **Filter**: Apply predicate function to select desired components
- **Join**: Reassemble filtered components with `.join()` method
- Essential pattern for selective text processing

#### Lambda Predicate Functions
- Use lambda functions as filter criteria: `lambda x: not x.startswith("-")`
- Predicate must return boolean (True to keep, False to remove)
- Enables inline filtering logic without separate function definitions
- Combines filter concept with lambda function mastery

#### Edge Case Handling in Text Processing
- Consider empty lines and special characters in filtering logic
- Preserve document structure including trailing newlines
- Test with various input patterns to ensure robustness
- Critical thinking about boundary conditions

#### Functional Text Processing Applications
- Document cleanup and content filtering
- Removing unwanted lines or sections from text
- Selective data extraction from structured text
- Maintaining document formatting during processing

## Project Structure Notes

- Repository contains mix of completed exercises (01, 04, 05, 07, CH2-L1, CH2-L2, CH2-L3, CH2-L4, CH2-L6) and lesson materials
- Complete Chapter 2: First-Class Functions with all lessons implemented and tested
- CH2-L4 and L6 introduce Python's built-in functional programming tools (map, filter, reduce trilogy)
- Some directories (06) contain only lesson content without implementations
- `Lecture.md` provides Vietnamese language context on Python's limitations for functional programming
- `learnlua.lua` file present but not part of main exercise structure