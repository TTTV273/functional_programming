# Why Curry?

It's fairly obvious that:

```py
def sum(a, b):
  return a + b
```

is simpler than:

```py
def sum(a):
  def inner_sum(b):
    return a + b
  return inner_sum
```

So why would we *ever* want to do the more complicated thing? Well, currying is often used to **change a function's signature** to make it conform to a specific shape. For example:

```py
def colorize(converter, doc):
  # ...
  converter(doc)
  # ...
```

The `colorize` function accepts a function called `converter` as input, and at some point during its execution, it calls `converter` with a single argument. That means that it expects `converter` to accept exactly one argument. So, if I have a conversion function like this:

```py
def markdown_to_html(doc, asterisk_style):
  # ...
```

I can't pass `markdown_to_html` to `colorize` because `markdown_to_html` wants *two* arguments. To solve this problem, I can curry `markdown_to_html` into a function that takes a single argument:

```py
def markdown_to_html(asterisk_style):
  def asterisk_md_to_html(doc):
    # do stuff with doc and asterisk_style...

  return asterisk_md_to_html

markdown_to_html_italic = markdown_to_html('italic')
colorize(markdown_to_html_italic, doc)
```

## Gemini Translation

Chào anh, em đã đọc và dịch xong bài học mới. Bài này giải thích lý do tại sao Currying lại hữu ích, dù trông có vẻ phức tạp hơn ban đầu.

-----

### **Tại sao nên dùng Currying?**

Rõ ràng là:

```python
def sum(a, b):
  return a + b
```

trông đơn giản hơn là:

```python
def sum(a):
  def inner_sum(b):
    return a + b
  return inner_sum
```

Vậy tại sao chúng ta lại muốn làm theo cách phức tạp hơn? Vâng, currying thường được dùng để **thay đổi "chữ ký" (signature) của một hàm** để làm cho nó phù hợp với một khuôn mẫu cụ thể.

Ví dụ:

```python
def colorize(converter, doc):
  # ...
  converter(doc)
  # ...
```

Hàm `colorize` chấp nhận một hàm khác tên là `converter` làm đầu vào, và tại một thời điểm nào đó, nó gọi hàm `converter` với một đối số duy nhất. Điều đó có nghĩa là nó kỳ vọng `converter` phải là một hàm chỉ chấp nhận đúng một đối số.

Vì vậy, nếu em có một hàm chuyển đổi như thế này:

```python
def markdown_to_html(doc, asterisk_style):
  # ...
```

Em không thể truyền hàm `markdown_to_html` vào cho `colorize` được, bởi vì `markdown_to_html` cần tới *hai* đối số. Để giải quyết vấn đề này, em có thể "curry hóa" hàm `markdown_to_html` thành một hàm chỉ nhận một đối số duy nhất:

```python
def markdown_to_html(asterisk_style):
  def asterisk_md_to_html(doc):
    # làm gì đó với doc và asterisk_style...

  return asterisk_md_to_html

markdown_to_html_italic = markdown_to_html('italic')
colorize(markdown_to_html_italic, doc)
```

-----

Đây là bản dịch của bài học mới. Sau khi đọc xong, anh hãy chú ý vào dòng code này nhé:
`markdown_to_html_italic = markdown_to_html('italic')`

Theo anh, biến `markdown_to_html_italic` lúc này là gì? Nó là một giá trị, hay là một hàm? Và nếu là một hàm thì nó đang chờ nhận vào tham số nào tiếp theo?
