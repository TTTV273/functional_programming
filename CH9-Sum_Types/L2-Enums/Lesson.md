# Enums

Doing the admittedly weird `class` and `isinstance()` thing works, but it turns out, there's a better way in some cases. If you're trying to represent a fixed set of values (but not store additional data within them) [enums](https://docs.python.org/3/library/enum.html) are the way to go.

Let's say we have a `Color` variable that we want to restrict to only three possible values:

- `RED`
- `GREEN`
- `BLUE`

We could use a plain-old `string` to represent these values, but that's annoying because we have to remember all the "valid" values and defensively check for invalid ones all over our codebase. Instead, we can use an `Enum`:

```py
from enum import Enum

Color = Enum('Color', ['RED', 'GREEN', 'BLUE'])
print(Color.RED)  # this works, prints 'Color.RED'
print(Color.TEAL) # this raises an exception
```

Now `Color` is a sum type! _At least, as close as we can get in Python._

There are a few benefits:

1. A "Color" can only be `RED`, `GREEN`, or `BLUE`. If you try to use `Color.TEAL`, Python raises an exception.
2. There is a central place to see the "valid" values for a `Color`.
3. Each "Color" has a "name" (e.g. `Color.RED`) and a "value" (e.g. `1`). The value is an integer and is used under the hood instead of the name. Integers take up less memory than strings, which helps with performance.

## Assignment

Create an `Enum` called `Doctype` with values:

- PDF
- TXT
- DOCX
- MD
- HTML

## Tip

Don't forget to `import` the `Enum` class from the `enum` module!

## Gemini Translation

Tất nhiên rồi, tôi rất sẵn lòng. Dưới đây là nội dung bài học đã được dịch sang tiếng Việt:

-----

### Enums (Kiểu liệt kê)

Việc sử dụng `class` và `isinstance()` tuy có phần "kỳ quặc" nhưng vẫn hoạt động. Tuy nhiên, trong một số trường hợp, có một cách tốt hơn. Nếu bạn đang cố gắng biểu diễn một tập hợp các giá trị cố định (mà không cần lưu trữ dữ liệu bổ sung trong chúng), thì [enums](https://docs.python.org/3/library/enum.html) (kiểu liệt kê) là lựa chọn phù hợp.

Giả sử chúng ta có một biến `Color` (Màu sắc) mà chúng ta muốn giới hạn chỉ trong ba giá trị có thể có:

- `RED` (Đỏ)
- `GREEN` (Xanh lá)
- `BLUE` (Xanh dương)

Chúng ta có thể sử dụng kiểu `string` (chuỗi) thông thường để biểu diễn các giá trị này, nhưng điều đó khá phiền phức vì chúng ta phải nhớ tất cả các giá trị "hợp lệ" và phải kiểm tra phòng ngừa các giá trị không hợp lệ ở khắp nơi trong mã nguồn. Thay vào đó, chúng ta có thể sử dụng một `Enum`:

```py
from enum import Enum

Color = Enum('Color', ['RED', 'GREEN', 'BLUE'])
print(Color.RED)  # hoạt động, in ra 'Color.RED'
print(Color.TEAL) # dòng này sẽ gây ra lỗi (exception)
```

Bây giờ, `Color` đã là một kiểu tổng hợp (sum type)! *Ít nhất, đây là cách gần nhất chúng ta có thể đạt được trong Python.*

Có một vài lợi ích:

1. Một "Color" chỉ có thể là `RED`, `GREEN`, hoặc `BLUE`. Nếu bạn cố gắng sử dụng `Color.TEAL`, Python sẽ báo lỗi.
2. Có một nơi tập trung để xem tất cả các giá trị "hợp lệ" cho một `Color`.
3. Mỗi "Color" có một "tên" (ví dụ: `Color.RED`) và một "giá trị" (ví dụ: `1`). Giá trị này là một số nguyên và được sử dụng ngầm thay cho tên. Số nguyên chiếm ít bộ nhớ hơn chuỗi, giúp cải thiện hiệu suất.

#### Bài tập

Tạo một `Enum` tên là `Doctype` với các giá trị:

- PDF
- TXT
- DOCX
- MD
- HTML

#### Gợi ý

Đừng quên `import` lớp `Enum` từ mô-đun `enum` nhé!

-----

Bây giờ sau khi đã hiểu rõ hơn về bài học, anh cho tôi biết dòng mã đầu tiên chúng ta cần viết trong tệp `main.py` là gì nhỉ?
