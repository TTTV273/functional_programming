# Build a Stateful Counter (with Closures)

Complete two functions that use Python closures.

## 1. make_counter(start=0, step=1) -> (next_count, reset, peek)

Returns three functions that share state via a closure:
- **next_count()**: returns the current value, then advances by step
- **reset(new_start=None)**: resets the current value
  - If new_start is provided, set current to new_start
  - If new_start is None, reset to the original start passed to make_counter
  - Returns the new current value
- **peek()**: returns the current value without changing it

Use a closure and the nonlocal keyword to mutate the shared state.

## 2. make_prefixer(prefix)

Returns a function that takes a message string and returns "{prefix} {message}".
Demonstrates a simple higher-order function and closure.

## Examples:

```python
# Counter usage
next_c, reset_c, peek_c = make_counter(10, 5)
print(peek_c())   # 10
print(next_c())   # 10  (then current becomes 15)
print(next_c())   # 15  (then current becomes 20)
print(peek_c())   # 20
print(reset_c())  # 10  (reset to original start)
print(peek_c())   # 10

# Prefixer usage
info = make_prefixer("[INFO]")
print(info("Server started"))   # [INFO] Server started
```

## Requirements:

- Use closures only; do not use classes or global variables.
- Use nonlocal in make_counter to update the stored state.
- Do not print from your functions.

## Gemini Translation

### Xây dựng một Bộ đếm có Trạng thái (với Closure)

Hoàn thành hai hàm sử dụng closure trong Python.

#### 1. make_counter(start=0, step=1) -> (next_count, reset, peek)

Hàm này trả về **ba hàm con**, tất cả đều chia sẻ trạng thái thông qua một closure:
* **next_count()**: trả về giá trị hiện tại, *sau đó* tăng giá trị lên theo `step`.
* **reset(new_start=None)**: đặt lại giá trị hiện tại.
    * Nếu `new_start` được cung cấp, đặt giá trị hiện tại thành `new_start`.
    * Nếu `new_start` là `None`, đặt lại về giá trị `start` ban đầu.
    * Trả về giá trị hiện tại mới.
* **peek()**: trả về giá trị hiện tại mà không thay đổi nó.

#### 2. make_prefixer(prefix)

Hàm này trả về một hàm con. Hàm con đó nhận một chuỗi `message` và trả về chuỗi `"{prefix} {message}"`.

---
Đây là một bài tập tổng hợp rất hay, đặc biệt là hàm `make_counter` vì nó trả về nhiều hàm con cùng chia sẻ một "trí nhớ".

Để bắt đầu, anh em mình sẽ tập trung vào hàm `make_counter` trước. Biến "trí nhớ" chính mà cả ba hàm con cần chia sẻ là gì ạ?