# More Transformations

Here's some example code for you to reference as you work through the assignment:

```python
def multiply(x, y):
    return x * y

def add(x, y):
    return x + y

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

## Assignment

Complete the `doc_format_checker_and_converter` function.

It takes a `conversion_function` and a list of `valid_formats` as parameters. It should return a *new* function that takes two parameters of its own:

*   `filename`: The name of the file to be converted
*   `content`: The content (body text) of the file to be converted

1.  [ ] If the file extension of the `filename` is in the `valid_formats` list, then it should return the result of calling the `conversion_function` on the `content`.
2.  [ ] Otherwise, it should [raise](https://docs.python.org/3/tutorial/errors.html#raising-exceptions) a [ValueError](https://docs.python.org/3/library/exceptions.html#ValueError) with the message `invalid file format`.

## Tip

I used the [.split()](https://docs.python.org/3/library/stdtypes.html#str.split) method on the `filename` to get the file extension. You can use the `in` keyword to check if a value is in a list.

The `capitalize_content` and `reverse_content` are "conversion functions" that will be passed into our `doc_format_checker_and_converter` function by the tests.

## Gemini Translation

### Thêm các Biến đổi Hàm

Đây là một số mã ví dụ để bạn tham khảo khi thực hiện bài tập:

```python
def multiply(x, y):
    return x * y

def add(x, y):
    return x + y

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

#### Bài tập

Hoàn thành hàm `doc_format_checker_and_converter`.

Hàm này nhận một hàm `conversion_function` và một danh sách các `valid_formats` làm tham số. Nó sẽ trả về một hàm *mới* nhận hai tham số của riêng nó:

*   `filename`: Tên của tệp cần chuyển đổi
*   `content`: Nội dung (văn bản) của tệp cần chuyển đổi

- [ ] 1.  [ ] Nếu phần mở rộng của tệp `filename` nằm trong danh sách `valid_formats`, thì nó sẽ trả về kết quả của việc gọi hàm `conversion_function` trên `content`.
- [ ] 2.  [ ] Ngược lại, nó sẽ [raise](https://docs.python.org/3/tutorial/errors.html#raising-exceptions) một [ValueError](https://docs.python.org/3/library/exceptions.html#ValueError) với thông báo `invalid file format`.

#### Gợi ý

Tôi đã sử dụng phương thức [.split()](https://docs.python.org/5/library/stdtypes.html#str.split) trên `filename` để lấy phần mở rộng của tệp. Bạn có thể sử dụng từ khóa `in` để kiểm tra xem một giá trị có trong danh sách hay không.

Các hàm `capitalize_content` và `reverse_content` là các "hàm chuyển đổi" sẽ được truyền vào hàm `doc_format_checker_and_converter` của chúng ta bởi các bài kiểm thử.
