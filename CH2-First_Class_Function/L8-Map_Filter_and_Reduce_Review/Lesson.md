# Map, Filter, and Reduce Review

Higher-order functions like `map`, `filter`, and `reduce`, allow us to avoid stateful iteration and mutations of variables.

Take a look at this [imperative](https://en.wikipedia.org/wiki/Imperative_programming) code that calculates the [factorial](https://en.wikipedia.org/wiki/Factorial) of a number:

```python
def factorial(n):
    # a procedure that continuously multiplies
    # the current result by the next number
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
```

Here's the same factorial function using `reduce`:

```python
import functools

def factorial(n):
    return functools.reduce(lambda x, y: x * y, range(1, n + 1))
```

In the functional example, we're just combining functions to get the result we want. There's no need to reassign variables or keep track of the program's state in a loop.

A loop is inherently stateful. Depending on which iteration you're on, the `i` variable has a different value.

## Key Learning Points

### Imperative vs Functional Thinking

**Imperative approach** (how to do it):
- Step-by-step instructions
- Mutable state (variables change)
- Loops with counters
- Focus on the procedure

**Functional approach** (what to achieve):
- Declare the transformation
- Immutable data
- Function composition
- Focus on the result

### Why Functional is Better

1. **No State Management**: No need to track loop variables or intermediate results
2. **No Mutation**: Variables never change, reducing bugs
3. **Composable**: Easy to combine with other functions
4. **Declarative**: Code expresses what you want, not how to get it
5. **Parallel-Friendly**: No shared mutable state means easier concurrency

### The Power of Reduce for Accumulation

Reduce is perfect for any operation that:
- Starts with a collection
- Accumulates a single result
- Applies the same operation repeatedly

Examples: sum, product, maximum, string concatenation, factorial

## Gemini Translation

# Ôn tập về Map, Filter, và Reduce

Các **hàm bậc cao** (higher-order functions) như `map`, `filter`, và `reduce`, cho phép chúng ta tránh việc lặp đi lặp lại có trạng thái (stateful iteration) và sự thay đổi giá trị của biến (mutations of variables).

Hãy xem đoạn code theo phong cách **mệnh lệnh** ([imperative](https://en.wikipedia.org/wiki/Imperative_programming)) dùng để tính **giai thừa** ([factorial](https://en.wikipedia.org/wiki/Factorial)) của một số:

```python
def factorial(n):
    # một quy trình liên tục nhân
    # kết quả hiện tại với số tiếp theo
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
```

Và đây là hàm tính giai thừa tương tự nhưng sử dụng `reduce`:

```python
import functools

def factorial(n):
    return functools.reduce(lambda x, y: x * y, range(1, n + 1))
```

Trong ví dụ theo phong cách hàm, chúng ta chỉ đơn giản là kết hợp các hàm lại với nhau để có được kết quả mong muốn. Không cần phải gán lại giá trị cho biến hay theo dõi trạng thái của chương trình trong một vòng lặp.

Một vòng lặp về bản chất là **có trạng thái**. Tùy thuộc vào bạn đang ở lần lặp nào, biến `i` sẽ có một giá trị khác nhau.

## Những điểm chính cần học

### Tư duy Mệnh lệnh vs. Tư duy Hàm

**Tiếp cận mệnh lệnh** (làm như thế nào):

  * Hướng dẫn từng bước một.
  * Trạng thái có thể thay đổi (biến thay đổi giá trị).
  * Dùng vòng lặp với biến đếm.
  * Tập trung vào **quy trình**.

**Tiếp cận hàm** (đạt được cái gì):

  * Khai báo sự biến đổi.
  * Dữ liệu bất biến.
  * Kết hợp các hàm (function composition).
  * Tập trung vào **kết quả**.

### Tại sao Lập trình Hàm lại tốt hơn

1.  **Không quản lý trạng thái**: Không cần theo dõi các biến trong vòng lặp hay các kết quả trung gian.
2.  **Không thay đổi giá trị (Mutation)**: Các biến không bao giờ thay đổi, giúp giảm thiểu lỗi.
3.  **Có thể kết hợp (Composable)**: Dễ dàng kết hợp với các hàm khác.
4.  **Mang tính khai báo (Declarative)**: Code thể hiện điều bạn muốn, chứ không phải cách để đạt được nó.
5.  **Thân thiện với xử lý song song**: Không có trạng thái chung bị thay đổi nghĩa là xử lý đồng thời (concurrency) dễ dàng hơn.

### Sức mạnh của Reduce cho việc Tích lũy

`Reduce` là lựa chọn hoàn hảo cho bất kỳ hoạt động nào mà:

  * Bắt đầu với một tập hợp (collection).
  * Tích lũy lại thành một kết quả duy nhất.
  * Áp dụng lặp đi lặp lại cùng một hoạt động.

**Ví dụ**: tính tổng, tính tích, tìm giá trị lớn nhất, nối chuỗi, tính giai thừa.