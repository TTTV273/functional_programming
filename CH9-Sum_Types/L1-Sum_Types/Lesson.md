# Sum Types

Remember when I said, "Pure functions are my favorite part of functional programming"? Well, [sum types](https://en.wikipedia.org/wiki/Tagged_union) are a close second.

A "sum" type is the opposite of a "product" type. This Python object is an example of a _product_ type:

```py
man.studies_finance = True
man.has_trust_fund = False
```

The total number of combinations a `man` can have is `4`, the _product_ of `2 * 2`:

| studies_finance | has_trust_fund |
|----------------|----------------|
| True           | True           |
| True           | False          |
| False          | True           |
| False          | False          |

If we add a third attribute, perhaps a `has_blue_eyes` boolean, the total number of possibilities multiplies again, to `8`!

| studies_finance | has_trust_fund | has_blue_eyes |
|----------------|----------------|---------------|
| True           | True           | True          |
| True           | True           | False         |
| True           | False          | True          |
| True           | False          | False         |
| False          | True           | True          |
| False          | True           | False         |
| False          | False          | True          |
| False          | False          | False         |

But let's pretend that we live in a world where there are _really_ only [three types of people](https://www.youtube.com/watch?v=tEt0IuQJX2o) that our program cares about:

1. Dateable
2. Undateable
3. Maybe dateable

We can _reduce_ the number of cases our code needs to handle by using a (admittedly fake Pythonic) sum type with only 3 possible _types_:

```py
class Person:
    def __init__(self, name):
        self.name = name

class Dateable(Person):
    pass

class MaybeDateable(Person):
    pass

class Undateable(Person):
    pass
```

Then we can use the [isinstance](https://docs.python.org/3/library/functions.html#isinstance) built-in function to check if a `Person` is an instance of one of the subclasses. It's a clunky way to represent sum types, but hey, it's Python.

```py
def respond_to_text(guy_at_bar):
    if isinstance(guy_at_bar, Dateable):
        return f"Hey {guy_at_bar.name}, I'd love to go out with you!"
    elif isinstance(guy_at_bar, MaybeDateable):
        return f"Hey {guy_at_bar.name}, I'm busy but let's hang out sometime later."
    elif isinstance(guy_at_bar, Undateable):
        return "Have you tried being rich?"
    else:
        raise ValueError("invalid person type")
```

## Sum Types

As opposed to product types, which can have many (often infinite) combinations, sum types have a _fixed_ number of possible values. To be clear: **Python doesn't really support sum types**. We have to use a workaround and invent our own little system and enforce it ourselves.

## Assignment

Whenever a document is parsed by Doc2Doc, it can either succeed or fail. In functional programming, we often represent errors as data (e.g. the `ParseError` class) rather than by `raise`ing exceptions, because exceptions are side effects. _(This isn't standard Python practice, but it's useful to understand from an FP perspective)_

**Complete the `Parsed` and `ParseError` subclasses.**

- `Parsed` represents success. It should accept a `doc_name` string and a `text` string and save them as properties of the same name.
- `ParseError` represents failure. It should accept a `doc_name` string and an `err` string and save them as properties of the same name.

The test suite uses the `isinstance` function to see if an error occurred based on the class type.

## Gemini Translation

Tất nhiên rồi. Để hiểu rõ hơn về khái niệm này, chúng ta hãy cùng xem qua nội dung của `Lesson.md` bằng tiếng Việt nhé.

-----

### Kiểu Tổng (Sum Types)

Bạn còn nhớ khi tôi nói, "Hàm thuần túy là phần tôi yêu thích nhất trong lập trình hàm" không? Vâng, [kiểu tổng (sum types)](https://en.wikipedia.org/wiki/Tagged_union) chỉ đứng thứ hai một chút thôi.

"Kiểu tổng" (sum type) là đối lập của "kiểu tích" (product type). Đối tượng Python này là một ví dụ về *kiểu tích*:

```py
man.studies_finance = True
man.has_trust_fund = False
```

Tổng số tổ hợp mà một đối tượng `man` có thể có là `4`, tức là *tích* của `2 * 2`:

| studies_finance | has_trust_fund |
| :--- | :--- |
| True | True |
| True | False |
| False | True |
| False | False |

Nếu chúng ta thêm một thuộc tính thứ ba, có lẽ là `has_blue_eyes`, tổng số khả năng lại nhân lên, thành `8`!

| studies_finance | has_trust_fund | has_blue_eyes |
| :--- | :--- | :--- |
| True | True | True |
| True | True | False |
| True | False | True |
| True | False | False |
| False | True | True |
| False | True | False |
| False | False | True |
| False | False | False |

Nhưng hãy giả vờ rằng chúng ta sống trong một thế giới nơi chương trình của chúng ta chỉ quan tâm đến *thực sự* [ba loại người](https://www.youtube.com/watch?v=tEt0IuQJX2o):

1. Có thể hẹn hò (Dateable)
2. Không thể hẹn hò (Undateable)
3. Có lẽ có thể hẹn hò (Maybe dateable)

Chúng ta có thể *giảm* số trường hợp mà code cần xử lý bằng cách sử dụng một kiểu tổng (thừa nhận là một kiểu Python giả) chỉ với 3 *kiểu* có thể có:

```py
class Person:
    def __init__(self, name):
        self.name = name

class Dateable(Person):
    pass

class MaybeDateable(Person):
    pass

class Undateable(Person):
    pass
```

Sau đó, chúng ta có thể sử dụng hàm tích hợp sẵn [isinstance](https://docs.python.org/3/library/functions.html#isinstance) để kiểm tra xem một `Person` có phải là một thực thể của một trong các lớp con hay không. Đó là một cách thể hiện kiểu tổng hơi cồng kềnh, nhưng mà, đây là Python mà.

```py
def respond_to_text(guy_at_bar):
    if isinstance(guy_at_bar, Dateable):
        return f"Chào {guy_at_bar.name}, em rất muốn đi chơi với anh!"
    elif isinstance(guy_at_bar, MaybeDateable):
        return f"Chào {guy_at_bar.name}, em bận rồi nhưng lúc khác chúng ta đi chơi nhé."
    elif isinstance(guy_at_bar, Undateable):
        return "Anh đã thử làm người giàu chưa?"
    else:
        raise ValueError("loại người không hợp lệ")
```

### Kiểu Tổng (Sum Types)

Trái ngược với kiểu tích, có thể có nhiều (thường là vô hạn) tổ hợp, kiểu tổng có một số lượng giá trị có thể có là **cố định**. Để rõ ràng: **Python không thực sự hỗ trợ kiểu tổng**. Chúng ta phải sử dụng một giải pháp thay thế, tự phát minh ra hệ thống nhỏ của riêng mình và tự thực thi nó.

### Bài tập

Bất cứ khi nào một tài liệu được phân tích bởi Doc2Doc, nó có thể thành công hoặc thất bại. Trong lập trình hàm, chúng ta thường biểu diễn lỗi dưới dạng dữ liệu (ví dụ: lớp `ParseError`) thay vì `raise` ngoại lệ, bởi vì ngoại lệ là các hiệu ứng phụ (side effects). *(Đây không phải là thực hành tiêu chuẩn trong Python, nhưng rất hữu ích để hiểu từ góc độ lập trình hàm)*

**Hãy hoàn thành các lớp con `Parsed` và `ParseError`.**

- `Parsed` đại diện cho thành công. Nó nên chấp nhận một chuỗi `doc_name` và một chuỗi `text` và lưu chúng thành các thuộc tính có cùng tên.
- `ParseError` đại diện cho thất bại. Nó nên chấp nhận một chuỗi `doc_name` và một chuỗi `err` và lưu chúng thành các thuộc tính có cùng tên.

Bộ kiểm thử sử dụng hàm `isinstance` để xem liệu có lỗi xảy ra hay không dựa trên kiểu của lớp.

-----

Bây giờ, khi đã hiểu rõ hơn về yêu cầu, chúng ta hãy quay lại với lớp `Parsed` nhé. Lớp này cần khởi tạo những thuộc tính nào để thể hiện một kết quả phân tích tài liệu thành công?
