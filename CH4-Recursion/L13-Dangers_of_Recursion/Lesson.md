# Dangers of Recursion

Recursion is great because it's simple and elegant, often being the most straightforward way to solve a problem. But there are some things to watch out for:

1. **Stack Overflow**: Each function call requires a bit of memory. So, if you recurse too deeply, you can run out of ["stack" memory](https://en.wikipedia.org/wiki/Stack-based_memory_allocation) which will crash your program. (This is what the famous [website](https://stackoverflow.com/) is named after)

2. If you don't have a solid base case, you can end up in an infinite loop (which will likely lead to a stack overflow).

3. Recursion (especially in a language like Python) is often slower than a `for` loop because each function call requires some memory. [Tail call optimization](https://exploringjs.com/es6/ch_tail-calls.html) can help with this, but Python doesn't support it.