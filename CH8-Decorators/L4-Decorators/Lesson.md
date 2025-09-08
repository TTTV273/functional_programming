# Decorators

The `*args` and `**kwargs` syntax is great for decorators that are intended to work on functions with different [signatures](https://developer.mozilla.org/en-US/docs/Glossary/Signature/Function).

## Example

The `log_call_count` function below doesn't care about the number or type of the decorated function's (`func_to_decorate`) arguments. It just wants to count how many times the function is called. However, it still needs to pass any arguments through to the wrapped function.

```python
def log_call_count(func_to_decorate):
    count = 0

    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"Called {count} times")
        # The * and ** syntax unpacks the arguments
        # and passes them to the decorated function
        return func_to_decorate(*args, **kwargs)

    return wrapper
```

## Assignment

**Complete the `markdown_to_text_decorator` function.** It can decorate a function with *any number of string arguments*, no matter if they're positional or keyword args. It will run the decorated function, but first strip out any Markdown heading symbols (see below for an explanation of Markdown headings).

It should `return` a `wrapper` function that takes `*args` and `**kwargs`. The wrapper should:

1. [Map](https://docs.python.org/3/library/functions.html#map) the `*args` to a new [list](https://docs.python.org/3/library/stdtypes.html#list) where each string is converted to plain text using `convert_md_to_txt`.
2. [Map](https://docs.python.org/3/library/functions.html#map) the `**kwargs` to a new [dictionary](https://docs.python.org/3/library/stdtypes.html#dict) where each "value" is converted to plain text using `convert_md_to_txt`. The "key" should remain the same.
   - Use the [`.items()`](https://docs.python.org/3/library/stdtypes.html#dict.items) dictionary method to pass a list of tuples of `key-value` pairs to map
   - Create a function for `map` which changes the `value` of an item tuple with `convert_md_to_txt`
3. Return the result of calling the decorated function with the new arguments.

## Tips

- Take a look at the editor's `formatters.py` file tab to see what the formatter functions do. What arguments are they expecting? You can use `*` tuple unpacking and `**` dictionary unpacking operators to pass variables as the correct arguments.
- The provided `convert_md_to_txt` function takes a string of [Markdown](https://www.markdownguide.org/cheat-sheet/) text and returns a string of text with any "heading" symbols removed. For example:

| Input | Output |
|-------|---------|
| `# This is a heading` | `This is a heading` |
| `## This is also a heading` | `This is also a heading` |
| `This is not a heading` | `This is not a heading` |
| `* This is also not a heading` | `* This is also not a heading` |

## Gemini Translation

### Decorators

Cú pháp `*args` và `**kwargs` rất tuyệt vời cho các decorator dùng để "bọc" các hàm có "chữ ký" (signatures) khác nhau.

#### Ví dụ

Hàm `log_call_count` dưới đây không quan tâm đến số lượng hay loại tham số của hàm được bọc (`func_to_decorate`). Nó chỉ muốn đếm số lần hàm đó được gọi. Tuy nhiên, nó vẫn cần truyền mọi tham số qua cho hàm được bọc.

```python
def log_call_count(func_to_decorate):
    count = 0

    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"Đã gọi {count} lần")
        # Cú pháp * và ** sẽ giải nén các tham số
        # và truyền chúng vào hàm được bọc
        return func_to_decorate(*args, **kwargs)

    return wrapper
```

#### Yêu cầu

**Hoàn thành hàm `markdown_to_text_decorator`.** Nó có thể "bọc" một hàm với *bất kỳ số lượng tham số chuỗi nào*, dù là tham số vị trí hay tham số có tên. Nó sẽ chạy hàm được bọc, nhưng trước tiên sẽ loại bỏ các ký hiệu tiêu đề Markdown (xem giải thích về tiêu đề Markdown bên dưới).

Nó nên `return` một hàm `wrapper` nhận vào `*args` và `**kwargs`. Hàm `wrapper` này nên:

1. Dùng hàm `map()` để xử lý `*args` thành một `list` mới, trong đó mỗi chuỗi được chuyển đổi thành văn bản thuần túy bằng `convert_md_to_txt`.
2. Dùng hàm `map()` để xử lý `**kwargs` thành một `dictionary` mới, trong đó mỗi "value" được chuyển đổi thành văn bản thuần túy bằng `convert_md_to_txt`. "key" sẽ được giữ nguyên.
   - Sử dụng phương thức `.items()` của dictionary để truyền một danh sách các cặp `key-value` dạng tuple vào `map`.
   - Tạo một hàm cho `map` để thay đổi `value` của một item tuple bằng `convert_md_to_txt`.
3. Trả về kết quả của việc gọi hàm được bọc với các tham số mới.

**Câu hỏi từ Gemini:** Trước khi chúng ta viết code, bạn có thể cho mình biết hàm `map()` trong Python thường dùng để làm gì không?
