# Project Overview

This is a functional programming exercise repository focused on Python implementations. The project is structured as numbered exercises (01, 02, 04, 05, 07, etc.) and chapter-based lessons (CH2-First_Class_Function/) where each directory contains:

- `main.py` - The primary implementation file with the exercise solution
- `main_test.py` - Test suite with predefined test cases and a custom testing framework
- `Lesson.md` - Educational content and exercise instructions (in lesson directories)

## Testing Framework

Each exercise uses a custom testing framework with two test case sets: `run_cases` (basic) and `submit_cases` (complete).

- **Run basic tests**: `python -c "__RUN__ = True; exec(open('main_test.py').read())"`
- **Run full suite**: `python main_test.py`

The framework validates outputs and ensures input immutability.

## Development Workflow

1.  Implement the solution in `main.py`.
2.  Test with basic cases.
3.  Test with the full suite.
4.  Ensure all tests pass and inputs are not modified.

---
## Gemini Added Memories

- The user prefers to communicate in Vietnamese.
- When collaborating with another AI in the same workspace, prefer a file-based workflow (one agent writes to a file, the other reads it) over using IPC messaging or file sharing tools for sharing information.

---
## Lesson Log

### CH1-L13: Ternary Expressions
- **Status**: Completed
- **Key Concepts**:
    - Refactored an `if/else` block to a single-line ternary expression.
    - Analyzed a test file to understand structural requirements (using `ast`).
    - Discussed the connection between expressions, purity, and side-effect control.
- **Process**:
    - Established and followed a 4-step learning plan (Analyze, Fail, Implement, Pass, Connect).
    - The plan was successfully reviewed and enhanced by `claude-fp`.
- **Collaboration**:
    - Successfully used IPC to have `claude-fp` review translation and the learning plan.