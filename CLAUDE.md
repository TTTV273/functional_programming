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

### Reduce Function (CH2-L7)
Based on completed lesson with Python's built-in reduce function:

#### Built-in Reduce Function Concept
- Python's `functools.reduce(function, iterable)` accumulates values into single result
- Acts as "snowball effect" - starts small and grows by accumulating each element
- Takes reducing function with two parameters: accumulator and next item
- Core functional programming tool that completes the map-filter-reduce trilogy

#### Accumulator Pattern Mastery
- **First Element**: Used as initial accumulator value automatically
- **Reducing Function**: Takes (accumulator, next_item) and returns new accumulator
- **Step-by-Step Growth**: Each iteration builds on previous accumulated result
- **Final Result**: Single value representing all elements combined

#### Helper Function Design
- Create simple combining functions like `join(doc_so_far, sentence)`
- Focus on single-step transformation between accumulator and new item
- Use clear parameter names that reflect accumulation pattern
- Return new accumulated value for next iteration

#### Edge Case Handling Excellence
- Empty inputs: Check for n=0 conditions before reduce operations
- Single item lists: Reduce handles gracefully (returns the single item)
- Boundary conditions: Use list slicing for partial processing
- Error prevention: Validate inputs before applying reduce

#### Debug-Driven Development
- Strategic print statements to visualize accumulator growth
- Understanding reduce execution flow through step-by-step observation
- Syntax precision: Identifying and correcting formatting issues
- Clean debugging that enhances learning without cluttering final code

#### Functional Programming Trilogy Completion
- **Map**: Transform all elements (one-to-one)
- **Filter**: Select some elements (many-to-fewer)  
- **Reduce**: Accumulate to single result (many-to-one)
- **Combined Power**: Chain operations for complex data processing

### Reduce Practice Mastery (L7-Reduce-Practice)
Based on comprehensive hands-on practice with 5 progressive exercises:

#### Advanced Accumulator Patterns
- **Numbers**: `reduce(add, numbers)` - Basic accumulation without starting value
- **Comparison**: `reduce(max_func, numbers)` - Finding extremes through comparison
- **Dictionaries**: `reduce(count_func, words, {})` - Building complex data structures
- **Lists**: `reduce(flatten_func, lists, [])` - Combining nested structures
- **Conditional Strings**: `reduce(url_func, parts)` - Complex formatting with edge cases

#### Starting Value Decision Matrix
- **Same Type Accumulation**: No starting value needed (numbers, comparison)
- **Different Type Accumulation**: Starting value required (dict from strings, list from sublists)
- **First Element as Base**: Natural when first element serves as foundation (URL building)
- **Empty Container Start**: Required when building from scratch (counting, flattening)

#### Debug-Driven Reduce Development
- Strategic print statements to visualize accumulator growth
- Step-by-step observation of "snowball effect" across data types
- Understanding reduce execution flow through hands-on experimentation
- Iterative refinement based on test feedback and edge case discovery

#### Edge Case Handling Excellence
- Empty inputs and single-element lists
- String formatting with trailing/leading characters
- Conditional logic within accumulator functions
- Type-specific operations (dict updates, list concatenation, string manipulation)

#### Real-World Application Patterns
- **Word Frequency Counting**: Dictionary accumulation for text analysis
- **Data Flattening**: List processing for nested structure normalization
- **URL Construction**: String building with formatting rules and validation
- **Statistical Operations**: Numerical accumulation for data aggregation
- **Comparative Analysis**: Finding extremes and optimal values

#### Practice Achievement Metrics
- 25/25 tests passed across all 5 exercises
- Perfect implementation of 5 different accumulator patterns
- Mastery of both starting value and first-element patterns
- Advanced string processing with conditional logic
- Complete functional programming trilogy understanding

### Map, Filter, and Reduce Review (CH2-L8)
Based on completed advanced lesson comparing imperative vs functional paradigms:

#### Imperative vs Functional Programming Comparison
- **Imperative Approach**: Step-by-step procedures with mutable state and explicit loops
- **Functional Approach**: Declarative transformations with immutable data and function composition
- **Factorial Example**: Traditional loop vs `functools.reduce(lambda x, y: x * y, range(1, n + 1))`
- **Key Insight**: Functional code expresses WHAT you want, imperative shows HOW to do it

#### Advanced Function Composition Mastery
- **filter→map→reduce Pipeline**: Chain multiple operations elegantly without intermediate variables
- **Real Estate Contract Analysis**: Practical application with actual business data
- **calculate_total_rental_revenue()**: Perfect pipeline filtering active rentals, mapping to values, reducing to sum
- **get_high_value_sales()**: Advanced filtering with short-circuit evaluation and type safety

#### Multi-Metric Data Analysis Patterns
- **create_contract_summary()**: Four different metrics calculated functionally in single operation
- **Business Logic Integration**: Active vs expired contract distinctions for real-world relevance
- **Statistical Calculations**: Average rental prices with proper filtering and mathematical precision
- **Functional Counting**: Pure functional approach to frequency analysis

#### Advanced Reduce Pattern Mastery
- **Data Structure Building**: `group_contracts_by_type()` using reduce to construct complex dictionaries
- **List Accumulation Pattern**: Building grouped data `{'rental': [contracts], 'sale': [contracts]}`
- **Optimization Algorithms**: `find_best_contract()` using reduce for maximum value finding
- **Comparison Logic**: Contract value calculations (rental: monthly_rent × duration, sale: price)

#### Error Resolution and Debugging Excellence
- **Syntax Error Recognition**: Fixed function parameter definitions and variable scope issues
- **Logic Debugging**: Systematic approach to short-circuit evaluation and type safety
- **Step-by-Step Analysis**: Deep understanding of reduce execution flow and variable handling
- **Business Logic Validation**: Ensuring calculations match real-world requirements

#### Real-World Application Integration
- **Contract Revenue Analysis**: Direct application to rental property business
- **High-Value Filtering**: Investment decision support through functional data processing
- **Summary Statistics**: Business intelligence through functional programming patterns
- **Optimization Problems**: Finding best contracts using pure functional approaches

### Zip Function (CH2-L10)
Based on completed lesson with Python's built-in zip function for data correlation:

#### Zip Function Mastery
- **Data Correlation Concept**: Combining multiple iterables element-wise into tuples
- **Document Processing Pipeline**: `zip(doc_names, doc_formats)` → `filter(valid_formats)` pattern
- **Memory Efficiency**: Iterator-based processing with strategic `list()` conversions
- **Length Handling**: Automatic stopping at shortest iterable length

#### Zip + Filter Composition Pattern
- **Function Chaining**: `list(filter(lambda pair: pair[1] in valid_formats, zip(...)))`
- **Business Logic Integration**: Pairing filenames with formats for validation
- **Predicate Composition**: Complex filtering with tuple element access
- **Type Safety**: Short-circuit evaluation and proper tuple indexing

#### Real-World Document Applications
- **File Management**: Matching filenames with extensions and metadata
- **Data Validation**: Checking correspondence between parallel datasets
- **Configuration Mapping**: Pairing keys with values for dynamic setup
- **Coordinate Processing**: Working with (x, y) pairs and geographic data

### Higher-Order Functions Practice (CH2-L11)
Based on completed ultimate challenge with one-liner functional composition:

#### Advanced Function Composition Mastery
- **One-Line Implementation**: Complex logic in single expression with readable formatting
- **Pipeline Optimization**: Combine → Transform → Filter → Deduplicate flow
- **Multi-Step Processing**: `set(filter(lambda, map(lambda, originals + backups)))`
- **Elegant Code Structure**: Multi-line formatting maintaining single expression integrity

#### Document Restoration System
- **Case Normalization**: `.upper()` for consistent document comparison
- **Corruption Detection**: `.isdigit()` for automated invalid file identification
- **Data Merging**: Tuple concatenation for multiple source integration
- **Deduplication Strategy**: Set-based approach for efficient duplicate removal

#### Advanced Lambda Patterns
- **Complex Predicates**: `lambda doc: not doc.isdigit()` for business logic
- **Transformation Chains**: `lambda doc: doc.upper()` in composition context
- **Predicate Composition**: Multiple conditions in functional filtering
- **Type Conversion Strategy**: Strategic use of `set()` for both deduplication and result type

#### Performance and Scalability Excellence
- **Iterator Efficiency**: Lazy evaluation until final collection
- **Single Pass Processing**: All operations combined into one traversal
- **Memory Optimization**: No intermediate variables in composition
- **O(1) Set Operations**: Efficient deduplication and membership testing

#### Business Logic Integration Mastery
- **Data Validation Systems**: Automated corruption detection algorithms
- **Consistency Enforcement**: Case-insensitive document matching
- **Reliability Patterns**: Robust handling of mixed data sources
- **Scalability Design**: Pattern works for any number of document sources

#### Functional Programming Pinnacle Achievement
- **Complete Mastery**: Integration of all learned concepts (map, filter, reduce, zip, lambdas)
- **Real-World Applications**: Document processing with business requirements
- **Code Excellence**: Balance of conciseness, readability, and performance
- **Pattern Recognition**: Ability to identify and implement optimal functional solutions

### Pure Functions (CH3-L1, L2, L5)
Based on completed lessons with perfect test scores and Gemini collaboration:

#### Pure Functions Concept Mastery
- **"Reliable Black Boxes"**: Functions that don't interact with the outside world and aren't affected by it
- **Deterministic Behavior**: Same inputs always produce same outputs for predictable code
- **No Side Effects**: Functions never modify external state, global variables, or perform I/O operations
- **Easy Testing and Debugging**: Pure functions are isolated and predictable, making them simple to test and reason about

#### Pure Function Recognition Patterns
- **Example Analysis**: `multiply_by2()` (pure), `buy_car()` (impure - global modification), `roll_die()` (impure - randomness)
- **Purity Criteria**: Must satisfy both deterministic behavior AND no side effects
- **Common Violations**: Global variable access, random number generation, file I/O, console output
- **Benefits**: Easier testing, debugging, and code maintenance through predictability

#### Reference vs Value Excellence
- **Pass by Reference (Mutable)**: Lists, Dictionaries, Sets - "Google Docs link" analogy
- **Pass by Value (Immutable)**: Integers, Floats, Strings, Booleans, Tuples - "photocopy" analogy
- **Critical Insight**: Mutable types create shared references that can break function purity accidentally
- **Mental Model**: Reference = shared document, Value = independent copy

#### Dictionary Immutability Implementation
- **Perfect `.copy()` Usage**: `copy_default_formats = default_formats.copy()` pattern mastery
- **Pure Function Pattern**: Copy input → Modify copy → Return new dictionary
- **add_format() Success**: 7/7 tests passed with perfect immutability preservation
- **remove_format() Excellence**: Logical removal (set to False) without input mutation

#### Bilingual Learning Excellence
- **Vietnamese Technical Terms**: "Hàm thuần khiết", "tác dụng phụ", "tham chiếu vs tham trị"
- **Conceptual Analogies**: "Photocopy vs Google Docs link" for reference/value distinction
- **Gemini Collaboration**: Excellent learning partnership with detailed Vietnamese explanations
- **Cross-Language Mastery**: Technical concepts reinforced in both Vietnamese and English

#### Real-World Application Patterns
- **Settings Management**: Doc2Doc format preferences with immutable updates
- **Configuration Systems**: Safe dictionary modifications without affecting defaults
- **Data Protection**: Ensuring original data structures remain untouched
- **Functional Architecture**: Building reliable, predictable systems through pure function principles

#### Pass by Reference Impurity (CH3-L6)
Based on completed lesson reinforcing pure function concepts through negative examples:

- **Impurity Recognition**: Understanding functions that modify inputs through reference passing
- **Side Effect Identification**: Recognizing global variable modification as classic impurity pattern
- **Pure vs Impure Contrast**: Direct comparison of `.copy()` usage vs direct input mutation
- **Professional Development**: Understanding that pure function usage distinguishes good from great developers

#### Input and Output Side Effects (CH3-L8)
Based on completed lesson with I/O elimination implementation:

- **I/O as Side Effects**: Understanding that even `print()` breaks function purity through console output
- **Testing Challenges**: Recognition that I/O operations make functions untestable by automated test suites
- **Pure Function Transformation**: Successfully converted `convert_case` from printing to returning values
- **Text Processing Implementation**: Perfect case conversion (uppercase, lowercase, titlecase) with pure functions
- **Error Handling Excellence**: Proper input validation and unsupported format handling

#### I/O Containment Architecture (CH3-L9)
Based on completed lesson with bilingual Vietnamese learning:

- **I/O Sandwich Pattern**: Understanding Input → Pure Processing → Output architectural design
- **Pragmatic Approach**: I/O as "dirty but necessary" - containment rather than elimination strategy
- **System Architecture**: Clear separation between I/O operations and pure function cores
- **Vietnamese Technical Mastery**: "Kiến trúc I/O Sandwich", "Lớp Đầu Vào/Xử Lý/Đầu Ra" terminology
- **Practical Application**: Real-world program design with functional programming principles

#### No-Op and Function Composition Mastery (CH3-L11)
Based on completed lesson with advanced markdown processing implementation:

- **No-Op Recognition**: Understanding that functions without return values are either useless or impure
- **Hierarchical Function Design**: Perfect Document → Lines → Words processing architecture
- **Functional Composition Excellence**: Masterful use of `map()`, `split()`, `join()`, `strip()` without `.replace()`
- **Pure Function Implementation**: `remove_emphasis_from_word`, `remove_emphasis_from_line`, `remove_emphasis` functions
- **Text Processing Mastery**: Markdown emphasis removal from *, **, *** patterns using pure functional approaches
- **String Manipulation Patterns**: Perfect split → map → join pattern for text processing at multiple levels
- **Vietnamese Technical Learning**: "Hoạt động vô dụng" (no-op), "hàm không trong sạch" terminology mastery

#### Chapter 3 Achievement Metrics
- **Perfect Test Scores**: 6/6 tests (L1), 7/7 tests (L5), complete L8 I/O elimination, L11 functional composition
- **Pure Function Mastery**: Complete understanding of deterministic, side-effect-free functions across all contexts
- **Immutability Excellence**: Flawless handling of mutable data structures while maintaining purity
- **I/O Architecture**: Advanced understanding of containment strategies and system design
- **Function Composition**: Hierarchical processing systems using pure functional programming principles
- **Bilingual Technical Mastery**: Vietnamese and English terminology for advanced pure function concepts
- **Code Quality Evolution**: Writing higher quality, more predictable code through comprehensive pure function principles

## Project Structure Notes

- Repository contains mix of completed exercises (01, 04, 05, 07, CH2-L1, CH2-L2, CH2-L3, CH2-L4, CH2-L6, CH2-L7, L7-Reduce-Practice, CH2-L8, CH2-L10, CH2-L11, CH3-L1, CH3-L2, CH3-L5) and lesson materials
- Complete Chapter 2: First-Class Functions with all lessons implemented and tested
- Complete Chapter 3: Pure Functions with perfect test scores and bilingual Vietnamese-English learning
- CH2-L4, L6, and L7 complete Python's built-in functional programming trilogy (map, filter, reduce)
- L7-Reduce-Practice provides comprehensive hands-on practice with 5 progressive reduce exercises (25/25 tests passed)
- CH2-L8 advances to imperative vs functional comparison with real estate contract analysis applications
- CH2-L10 introduces zip function for data correlation and document processing pipelines
- CH2-L11 represents functional programming pinnacle with one-liner higher-order function composition mastery
- Some directories (06) contain only lesson content without implementations
- `Lecture.md` provides Vietnamese language context on Python's limitations for functional programming
- `learnlua.lua` file present but not part of main exercise structure