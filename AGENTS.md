# AGENTS.md - Repository Guidelines

## Build, Test & Development Commands
- **Run single test**: `python CH2-First_Class_Function/L4-Map/main_test.py`
- **Quick iteration**: Edit function in `main.py`, then run corresponding `main_test.py`
- No build system needed; files run directly with Python 3

## Project Structure 
- Chapters: `CH*-Topic/` directories with lessons as `L{n}-Topic/`
- Each lesson: `Lesson.md`, `main.py` (implementation), `main_test.py` (tests)
- Early exercises in numeric folders (`01/`, `02/`, etc.)

## Code Style & Conventions
- **Formatting**: 4-space indentation, `snake_case` for functions/variables
- **Imports**: Use `from main import *` in test files
- **Functions**: Pure functions preferred - no mutation, return new values
- **Comments**: Use `# TODO(human):` for implementation hints
- **Names**: Clear, lesson-aligned (e.g., `change_bullet_style`, `factorial_r`)

## Testing Patterns
- Tests use print-based assertions with `run_cases` (quick) and `submit_cases` (full)
- Test structure: input/expected tuples, custom `test()` function, pass/fail reporting
- Verify immutability when required (inputs unchanged after function calls)

## Functional Programming Principles
- Avoid side effects and I/O in core logic
- Keep functions small and composable
- Use higher-order functions (map, filter, reduce) appropriately
- Maintain referential transparency
