# No-Op

A [no-op](https://en.wikipedia.org/wiki/NOP_(code)) is an operation that does... nothing.

If a function doesn't return anything, it's probably impure. If it doesn't return anything, the only reason for it to exist is to perform a side effect.

## Example No-Op

This function performs a useless computation because it doesn't return anything or perform a side effect. It's a no-op.

```python
def square(x):
    x * x
```

## Example Side Effect

This function performs a side effect. It changes the value of the `y` variable that is outside of its scope. It's impure.

```python
y = 5
def add_to_y(x):
    global y
    y += x

add_to_y(3)
# y = 8
```

> **Note:** The [`global`](https://docs.python.org/3/reference/simple_stmts.html#global) keyword just tells Python to allow modification of the outer-scoped `y` variable.

## print()

Even the `print()` function (technically) has an impure side effect! It doesn't return anything, but it does print text to the console, which is a form of I/O.

## Assignment

Complete the `remove_emphasis`, `remove_emphasis_from_line`, and `remove_emphasis_from_word` functions.

`remove_emphasis` is the parent function. It takes a full document with any number of lines and removes any amount of `*` characters that are at the start or end of a word. ([Emphasis](https://www.markdownguide.org/basic-syntax/#emphasis) in Markdown)

For example, this:

```
I *love* markdown.
I **really love** markdown.
I ***really really love*** markdown
```

Should become:

```
I love markdown.
I really love markdown.
I really really love markdown
```

Write the helper functions, they will make the `remove_emphasis` function much easier to write:

- The `remove_emphasis_from_word` function should remove emphasis from a single word.
- The `remove_emphasis_from_line` function should split a given line into words and use the function we just created to remove emphasis from each word.

Don't forget to handle newline characters (`\n`) appropriately at the end of lines.

## Tips

For the sake of practice, try it without the `.replace()` string method. I used some of these built-ins:

- [str.split](https://docs.python.org/3/library/stdtypes.html#str.split)
- [str.strip](https://docs.python.org/3/library/stdtypes.html#str.strip)
- [join](https://docs.python.org/3/library/stdtypes.html#str.join)
- [map](https://docs.python.org/3/library/functions.html#map)

## Gemini Translation (Bản Dịch Gemini)

### **# No-Op**

Một [**no-op**](https://en.wikipedia.org/wiki/NOP_(code)) là một thao tác mà... không làm gì cả.

Nếu một hàm không trả về bất cứ thứ gì, nó có lẽ là một hàm không trong sạch. Nếu nó không trả về gì, lý do duy nhất để nó tồn tại là để thực hiện một tác dụng phụ.

### **## Ví dụ về No-Op**

Hàm này thực hiện một phép tính vô dụng vì nó không trả về bất cứ thứ gì hoặc thực hiện một tác dụng phụ. Nó là một no-op.

```python
def square(x):
    x * x
```

### **## Ví dụ về Tác dụng phụ**

Hàm này thực hiện một tác dụng phụ. Nó thay đổi giá trị của biến `y` nằm ngoài phạm vi của nó. Nó là một hàm không trong sạch.

```python
y = 5
def add_to_y(x):
    global y
    y += x

add_to_y(3)
# y bây giờ bằng 8
```

> **Lưu ý:** Từ khóa [`global`](https://docs.python.org/3/reference/simple_stmts.html#global) chỉ đơn giản là báo cho Python cho phép sửa đổi biến `y` ở phạm vi bên ngoài.

### **## Hàm print()**

Ngay cả hàm `print()` (về mặt kỹ thuật) cũng có một tác dụng phụ không trong sạch! Nó không trả về bất cứ thứ gì, nhưng nó in văn bản ra console, đó là một dạng của I/O.

### **## Bài tập**

Hoàn thành các hàm `remove_emphasis`, `remove_emphasis_from_line`, và `remove_emphasis_from_word`.

`remove_emphasis` là hàm cha. Nó nhận một tài liệu đầy đủ với bất kỳ số lượng dòng nào và loại bỏ bất kỳ số lượng ký tự `*` nào ở đầu hoặc cuối của một từ. (Đây là cú pháp [Nhấn mạnh](https://www.markdownguide.org/basic-syntax/#emphasis) trong Markdown).

Ví dụ, đoạn văn này:

```
I *love* markdown.
I **really love** markdown.
I ***really really love*** markdown
```

Nên trở thành:

```
I love markdown.
I really love markdown.
I really really love markdown
```

Hãy viết các hàm trợ giúp trước, chúng sẽ làm cho việc viết hàm `remove_emphasis` trở nên dễ dàng hơn nhiều:

* Hàm `remove_emphasis_from_word` nên loại bỏ nhấn mạnh khỏi một từ duy nhất.
* Hàm `remove_emphasis_from_line` nên tách một dòng đã cho thành các từ và sử dụng hàm chúng ta vừa tạo để loại bỏ nhấn mạnh khỏi mỗi từ.

Đừng quên xử lý các ký tự xuống dòng (`\n`) một cách thích hợp ở cuối các dòng.

### **## Gợi ý**

Để luyện tập, hãy thử làm bài này mà không dùng phương thức chuỗi `.replace()`. Tôi đã sử dụng một số hàm có sẵn sau:

* [str.split](https://docs.python.org/3/library/stdtypes.html#str.split)
* [str.strip](https://docs.python.org/3/library/stdtypes.html#str.strip)  
* [join](https://docs.python.org/3/library/stdtypes.html#str.join)
* [map](https://docs.python.org/3/library/functions.html#map)

## Nguyên Tắc Pure Functions Áp Dụng

- **Mỗi hàm phải `return` giá trị** - Không được là no-op
- **Không sửa đổi input** - Tạo output mới thay vì thay đổi input
- **Không có side effects** - Chỉ xử lý và trả về kết quả
- **Có thể test được** - Các hàm pure dễ kiểm thử và gỡ lỗi