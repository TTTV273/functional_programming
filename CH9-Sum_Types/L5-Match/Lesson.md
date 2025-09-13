# Match

Let's take another look at our example [Enum](https://docs.python.org/3/library/enum.html) from the previous lesson:

```py
Color = Enum("Color", ["RED", "GREEN", "BLUE"])
```

## Working With Enums

Python has a `match` statement that tends to be a lot cleaner than a series of `if/else/elif` statements when we're working with a fixed set of possible values (like a sum type, or more specifically an enum):

```py
def get_hex(color):
    match color:
        case Color.RED:
            return "#FF0000"
        case Color.GREEN:
            return "#00FF00"
        case Color.BLUE:
            return "#0000FF"

        # default case
        # (invalid Color)
        case _:
            return "#FFFFFF"
```

If you have _two_ values to match, you can use a `tuple`:

```py
def get_hex(color, shade):
    match (color, shade):
        case (Color.RED, Shade.LIGHT):
            return "#FFAAAA"
        case (Color.RED, Shade.DARK):
            return "#AA0000"
        case (Color.GREEN, Shade.LIGHT):
            return "#AAFFAA"
        case (Color.GREEN, Shade.DARK):
            return "#00AA00"
        case (Color.BLUE, Shade.LIGHT):
            return "#AAAAFF"
        case (Color.BLUE, Shade.DARK):
            return "#0000AA"

        # default case
        # (invalid combination)
        case _:
            return "#FFFFFF"
```

The value we want to compare is set after the `match` keyword, which is then compared against different cases/patterns. If a match is found, the code in the block is executed.

## Assignment

Complete the `convert_format` function. Using the enum `DocFormat`, it should support 3 types of conversions:

**From `MD` to `HTML`:**

Assume the content is a single `h1` tag in markdown syntax - it's a single string representing a line. Replace the leading `# ` with an `<h1>` and add a `</h1>` to the end.

`# This is a heading` -> `<h1>This is a heading</h1>`

**From `TXT` to `PDF`:**

Simply add a `[PDF]` tag to the beginning and end of the content. Notice the spaces between `[PDF]` tags and the content:

`This is some text` -> `[PDF] This is some text [PDF]`

**From `HTML` to `MD`:**

Replace any `<h1>` tags with `# ` and remove any `</h1>` tags.

`<h1>This is a heading</h1>` -> `# This is a heading`

**Any other conversion:**

If the input format is invalid, raise an `Exception` with the string `invalid type`.

## Gemini Translation

Tất nhiên rồi, đây là nội dung bài học được dịch sang tiếng Việt để anh tiện theo dõi.

-----

### Lệnh Match (Đối sánh)

Hãy cùng xem lại ví dụ về `Enum` của chúng ta từ bài học trước:

```py
Color = Enum("Color", ["RED", "GREEN", "BLUE"])
```

### Làm việc với Enums

Python có một lệnh `match` thường gọn gàng hơn nhiều so với một chuỗi các lệnh `if/else/elif` khi chúng ta làm việc với một tập hợp các giá trị cố định (như một kiểu tổng hợp, hoặc cụ thể hơn là một enum):

```py
def get_hex(color):
    match color:
        case Color.RED:
            return "#FF0000"
        case Color.GREEN:
            return "#00FF00"
        case Color.BLUE:
            return "#0000FF"

        # trường hợp mặc định
        # (Màu không hợp lệ)
        case _:
            return "#FFFFFF"
```

Nếu bạn có *hai* giá trị cần đối sánh, bạn có thể sử dụng một `tuple`:

```python
def get_hex(color, shade):
    match (color, shade):
        case (Color.RED, Shade.LIGHT):
            return "#FFAAAA"
        case (Color.RED, Shade.DARK):
            return "#AA0000"
        case (Color.GREEN, Shade.LIGHT):
            return "#AAFFAA"
        case (Color.GREEN, Shade.DARK):
            return "#00AA00"
        case (Color.BLUE, Shade.LIGHT):
            return "#AAAAFF"
        case (Color.BLUE, Shade.DARK):
            return "#0000AA"

        # trường hợp mặc định
        # (kết hợp không hợp lệ)
        case _:
            return "#FFFFFF"
```

Giá trị chúng ta muốn so sánh được đặt sau từ khóa `match`, sau đó nó được so sánh với các trường hợp/mẫu (`case`/`pattern`) khác nhau. Nếu tìm thấy một trường hợp khớp, đoạn mã trong khối đó sẽ được thực thi.

### Bài tập

Hoàn thành hàm `convert_format`. Sử dụng enum `DocFormat`, hàm này cần hỗ trợ 3 loại chuyển đổi:

**Từ `MD` sang `HTML`:**

Giả sử nội dung là một thẻ `h1` duy nhất theo cú pháp markdown - đó là một chuỗi duy nhất đại diện cho một dòng. Hãy thay thế `# ` ở đầu bằng `<h1>` và thêm `</h1>` vào cuối.

`# This is a heading` -> `<h1>This is a heading</h1>`

**Từ `TXT` sang `PDF`:**

Chỉ cần thêm thẻ `[PDF]` vào đầu và cuối nội dung. Lưu ý có khoảng trắng giữa thẻ `[PDF]` và nội dung:

`This is some text` -> `[PDF] This is some text [PDF]`

**Từ `HTML` sang `MD`:**

Thay thế bất kỳ thẻ `<h1>` nào bằng `# ` và xóa bỏ bất kỳ thẻ `</h1>` nào.

`<h1>This is a heading</h1>` -> `# This is a heading`

**Bất kỳ chuyển đổi nào khác:**

Nếu tổ hợp chuyển đổi không hợp lệ, hãy ném ra một `Exception` với chuỗi `invalid type`.

-----

Bây giờ sau khi đã có bản dịch, anh hãy xem lại các ví dụ. Từ khóa đầu tiên chúng ta cần dùng để bắt đầu kiểm tra hai biến `from_format` và `to_format` là gì nhỉ?
