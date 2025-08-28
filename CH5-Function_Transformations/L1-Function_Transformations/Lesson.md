# Function Transformations

"Function transformation" is just a more concise way to describe a specific type of [higher order function](https://en.wikipedia.org/wiki/Higher-order_function). It's when a function takes a function (or functions) as input and returns a *new* function. Let's look at an example:

```python
def multiply(x, y):
    return x * y

def add(x, y):
    return x + y

# self_math is a higher order function
# input: a function that takes two arguments and returns a value
# output: a new function that takes one argument and returns a value
def self_math(math_func):
    def inner_func(x):
        return math_func(x, x)
    return inner_func

square_func = self_math(multiply)
double_func = self_math(add)

print(square_func(5))
# prints 25

print(double_func(5))
# prints 10
```

The `self_math` function takes a function that operates on two *different* parameters (e.g. `multiply` or `add`) and returns a new function that operates on *one* parameter *twice* (e.g. `square` or `double`).

## Assignment

Doc2Doc needs a good logging system so that users and developers alike can see what's going on under the hood. **Complete the `get_logger` function.**

It takes a `formatter` function as a parameter and returns *a new function*. Steps:

1. [ ] Define a new function, `logger`, inside `get_logger` (see `self_math` above as an example). It accepts two strings. You can just name them `first` and `second` if you like.
2. [ ] The `logger` function should *not* return anything. It should simply `print` the result of calling the given `formatter` function with the `first` and `second` strings as arguments.
3. [ ] Return the new `logger` function for the test suite to use.

## Tip

The `colon_delimit` and `dash_delimit` functions are "formatters" that will be passed into our `get_logger` function by the tests. You don't need to touch them, but it's important to understand that when you call `formatter()` in the `get_logger` function, you're calling one of these functions.

## Gemini Translation

## Biến Đổi Hàm

"Biến đổi hàm" (Function Transformation) chỉ là một cách nói ngắn gọn hơn để mô tả một loại [hàm bậc cao](https://en.wikipedia.org/wiki/Higher-order_function) cụ thể. Đó là khi một hàm nhận đầu vào là một (hoặc nhiều) hàm khác và trả về một hàm *mới*. Hãy cùng xem một ví dụ:

```python
def multiply(x, y):
    return x * y

def add(x, y):
    return x + y

# self_math là một hàm bậc cao
# đầu vào: một hàm nhận hai tham số và trả về một giá trị
# đầu ra: một hàm mới nhận một tham số và trả về một giá trị
def self_math(math_func):
    def inner_func(x):
        return math_func(x, x)
    return inner_func

square_func = self_math(multiply)
double_func = self_math(add)

print(square_func(5))
# in ra 25

print(double_func(5))
# in ra 10
```

Hàm `self_math` nhận vào một hàm hoạt động trên hai tham số *khác nhau* (ví dụ: `multiply` hoặc `add`) và trả về một hàm mới hoạt động trên *một* tham số được dùng *hai lần* (ví dụ: `square` hoặc `double`).

-----

## Bài tập

Doc2Doc cần một hệ thống ghi log (logging) tốt để cả người dùng và lập trình viên đều có thể thấy được những gì đang diễn ra bên trong. **Hãy hoàn thành hàm `get_logger`.**

Hàm này nhận một hàm `formatter` làm tham số và trả về *một hàm mới*. Các bước thực hiện:

1.  Định nghĩa một hàm mới, đặt tên là `logger`, bên trong hàm `get_logger` (xem ví dụ với `self_math` ở trên). Hàm này chấp nhận hai chuỗi ký tự. Bạn có thể đặt tên chúng là `first` và `second`.
2.  Hàm `logger` sẽ *không* trả về bất cứ thứ gì. Nó chỉ đơn giản là `print` (in) ra kết quả của việc gọi hàm `formatter` đã cho với hai chuỗi `first` và `second` làm đối số.
3.  Trả về hàm `logger` mới để bộ kiểm thử (test suite) có thể sử dụng.

-----

## Gợi ý

Các hàm `colon_delimit` và `dash_delimit` là những "hàm định dạng" (formatters) sẽ được truyền vào hàm `get_logger` của chúng ta bởi các bài kiểm thử. Bạn không cần chỉnh sửa chúng, nhưng điều quan trọng là phải hiểu rằng khi bạn gọi `formatter()` bên trong hàm `get_logger`, bạn đang thực sự gọi một trong hai hàm này.
