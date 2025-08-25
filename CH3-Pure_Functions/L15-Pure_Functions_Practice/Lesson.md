# Pure Functions Practice

Doc2Doc is customizable. New commands can be configured to use whichever function suits the user. However, the new commands are causing bugs in other parts of the application by mutating global values and other unintended side effects.

## Assignment

Fix the following issues to make the functions pure:

1. `add_custom_command` is mutating an input
2. `add_format` is mutating an input
3. `save_document` is mutating an input
4. `add_line_break` has a side effect (printing to stdout) and no return value