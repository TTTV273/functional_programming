# Decorators Practice

You can stack decorators, and you can use currying with decorators.

```python
def to_uppercase(func):
    def wrapper(document):
        return func(document.upper())

    return wrapper

def get_truncate(length):
    def truncate(func):
        def wrapper(document):
            return func(document[:length])

        return wrapper

    return truncate

@to_uppercase
@get_truncate(9) # currying
def print_input(input):
    print(input)

print_input("Keep Calm and Carry On")
# prints: "KEEP CALM"
```

Observe that `to_uppercase` wrapped `get_truncate(9)`, and `get_truncate(9)` returned `truncate` which wrapped `print_input`, then `print_input` printed "KEEP CALM" from "Keep Calm and Carry On".

## Assignment

Doc2Doc needs a feature that can take care of encoding characters as [escape sequences](https://www.w3.org/MarkUp/html-spec/html-spec_9.html#SEC9.7.1) in HTML documents.

> **Tip**: You might not know anything about HTML. *That's fine*. This assignment isn't about HTML directly.
> 
> Just understand that it's a markup language like Markdown. Certain characters are interpreted as part of HTML syntax. In order to show these characters without interpreting them, they must be escaped, e.g., replace `"<"` with `"&lt;"`.

Complete the `replacer` function.

1. It takes as input two strings, `old` and `new`, and returns a function, `replace`.
2. `replace` takes an input function, `decorated_func`, and returns a `wrapper` function.
3. `wrapper` takes as input a string `text`. It uses `.replace()` string method to replace instances of `old` with `new` in the `text`. Then it returns the result of passing the modified `text` to the `decorated_func`.
4. Use a series of the `replacer` function to decorate `tag_pre`. Pass the following pairs of strings to these decorators to encode the escape sequences:
   1. Replace `"&"` with `"&amp;"`
   2. Replace `"<"` with `"&lt;"`
   3. Replace `">"` with `"&gt;"`
   4. Replace `'"'` with `"&quot;"`
   5. Replace `"'"` with `"&#x27;"`

## Gemini Translation

Tất nhiên rồi. Hiểu rõ yêu cầu trước khi làm là tốt nhất. Dưới đây là nội dung bài học được dịch sang tiếng Việt.

-----

# Thực hành Decorators

Bạn có thể **xếp chồng (stack)** các decorator, và bạn có thể sử dụng **currying** với decorator.

```python
def to_uppercase(func):
    def wrapper(document):
        return func(document.upper())

    return wrapper

def get_truncate(length):
    def truncate(func):
        def wrapper(document):
            return func(document[:length])

        return wrapper

    return truncate

@to_uppercase
@get_truncate(9) # currying
def print_input(input):
    print(input)

print_input("Keep Calm and Carry On")
# in ra: "KEEP CALM"
```

Hãy quan sát rằng `to_uppercase` đã bọc `get_truncate(9)`, `get_truncate(9)` trả về hàm `truncate`, hàm `truncate` này lại bọc hàm `print_input`, và cuối cùng `print_input` đã in ra "KEEP CALM" từ chuỗi "Keep Calm and Carry On".

## Nhiệm vụ

Doc2Doc cần một tính năng có thể xử lý việc mã hóa các ký tự thành [chuỗi thoát (escape sequences)](https://www.w3.org/MarkUp/html-spec/html-spec_9.html#SEC9.7.1) trong tài liệu HTML.

> **Mẹo**: Bạn có thể không biết gì về HTML. *Không sao cả*. Bài tập này không trực tiếp về HTML.
>
> Chỉ cần hiểu rằng nó là một ngôn ngữ đánh dấu giống như Markdown. Một số ký tự nhất định được hiểu là một phần của cú pháp HTML. Để hiển thị các ký tự này mà không bị diễn giải, chúng phải được "thoát", ví dụ: thay thế `"<"` bằng `"&lt;"`.

Hoàn thành hàm `replacer`.

1. Nó nhận đầu vào là hai chuỗi, `old` và `new`, và trả về một hàm, `replace`.
2. Hàm `replace` nhận một hàm đầu vào, `decorated_func`, và trả về một hàm `wrapper`.
3. Hàm `wrapper` nhận đầu vào là một chuỗi `text`. Nó sử dụng phương thức chuỗi `.replace()` để thay thế các lần xuất hiện của `old` bằng `new` trong `text`. Sau đó, nó trả về kết quả của việc truyền `text` đã được sửa đổi vào `decorated_func`.
4. Sử dụng một chuỗi các hàm `replacer` để trang trí cho `tag_pre`. Truyền các cặp chuỗi sau vào các decorator này để mã hóa các chuỗi thoát:
   1. Thay thế `"&"` bằng `"&amp;"`
   2. Thay thế `"<"` bằng `"&lt;"`
   3. Thay thế `">"` bằng `"&gt;"`
   4. Thay thế `'"'` bằng `"&quot;"`
   5. Thay thế `"'"` bằng `"&#x27;"`

-----

Sau khi anh đã sẵn sàng, hãy cho em biết nhé, và chúng ta sẽ bắt đầu với bước đầu tiên: xây dựng lớp ngoài cùng của hàm `replacer`.