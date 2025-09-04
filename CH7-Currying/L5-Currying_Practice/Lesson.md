# Currying Practice

Markdown makes [displaying images](https://www.markdownguide.org/basic-syntax/#images-1) as simple as possible. To add an image to a markdown document, just use this syntax:

```
![alt text](url "title")
```

- `alt text` a brief description for screen readers and web scrapers. Required for accessibility.
- `url` url or relative path to image.
- `title` shown on mouse hover. Optional.

## Assignment

Doc2Doc makes using markdown a breeze. This includes adding images to markdown documents.

Complete the `create_markdown_image` function using currying. It takes a string input, `alt_text`.

1. Enclose the `alt_text` in square brackets prefixed with an exclamation point `![alt_text]`.
2. Define an inner function that also takes a string input, `url`:
   1. The inner function should first escape any parentheses in the URL by replacing them with [encoded sequences](https://www.url-encode-decode.com/).
      1. Use the `.replace()` string method to change any opening parenthesis `(` into `%28`.
      2. Do the same to change any closing parenthesis `)` into `%29`.
   2. Enclose the `url` with parentheses `(url)`.
   3. Add the enclosed `url` to the end of the enclosed `alt_text`: `![alt_text](url)`
   4. Define the innermost function. It should take an optional string input for the `title` (`title=None`).
      1. If a `title` is passed:
         1. Enclose it in double quotes.
         2. Then add the quoted `title` to the image syntax by first removing the closing parenthesis `)` from the end of the image syntax.
         3. Add a space and the quoted `title` with a closing parenthesis `)` to the end of the image syntax: `![alt_text](url "title")`
      2. Return the finished image syntax.
   5. Return the innermost function
3. Return the inner function

## Gemini Translation

### Thực hành Currying

Markdown giúp việc [hiển thị hình ảnh](https://www.markdownguide.org/basic-syntax/#images-1) trở nên đơn giản nhất có thể. Để thêm một hình ảnh vào tài liệu markdown, bạn chỉ cần sử dụng cú pháp này:

```
![alt text](url "title")
```

  - `alt text`: một mô tả ngắn gọn cho các trình đọc màn hình (screen reader) và trình thu thập dữ liệu web. Bắt buộc để đảm bảo khả năng truy cập.
  - `url`: đường dẫn URL hoặc đường dẫn tương đối đến hình ảnh.
  - `title`: được hiển thị khi di chuột qua. Không bắt buộc.

#### Bài tập

Doc2Doc giúp việc sử dụng markdown trở nên cực kỳ dễ dàng. Điều này bao gồm cả việc thêm hình ảnh vào tài liệu markdown.

Hãy hoàn thành hàm `create_markdown_image` bằng cách sử dụng kỹ thuật **currying**. Hàm này nhận một chuỗi đầu vào là `alt_text`.

1.  Đặt `alt_text` trong cặp ngoặc vuông, với dấu chấm than ở phía trước: `![alt_text]`.
2.  Định nghĩa một hàm bên trong (`inner function`) cũng nhận một chuỗi đầu vào là `url`:
    1.  Hàm bên trong trước tiên nên **"thoát" (escape)** bất kỳ dấu ngoặc đơn nào trong URL bằng cách thay thế chúng bằng [các chuỗi đã được mã hóa](https://www.url-encode-decode.com/).
        1.  Sử dụng phương thức chuỗi `.replace()` để đổi bất kỳ dấu ngoặc đơn mở `(` nào thành `%28`.
        2.  Làm tương tự để đổi bất kỳ dấu ngoặc đơn đóng `)` nào thành `%29`.
    2.  Đặt `url` trong cặp ngoặc đơn `(url)`.
    3.  Thêm `url` đã được bọc trong ngoặc vào cuối của `alt_text` đã được bọc: `![alt_text](url)`
    4.  Định nghĩa hàm trong cùng nhất (`innermost function`). Hàm này nên nhận một chuỗi đầu vào không bắt buộc cho `title` (`title=None`).
        1.  Nếu một `title` được truyền vào:
            1.  Đặt nó trong cặp ngoặc kép.
            2.  Sau đó, thêm `title` đã được đặt trong ngoặc kép vào cú pháp hình ảnh bằng cách trước tiên **xóa dấu ngoặc đơn đóng `)`** khỏi cuối cú pháp.
            3.  Thêm một khoảng trắng và `title` đã được đặt trong ngoặc kép cùng với một dấu ngoặc đơn đóng `)` vào cuối cú pháp hình ảnh: `![alt_text](url "title")`
        2.  Trả về cú pháp hình ảnh đã hoàn thiện.
    5.  Trả về hàm trong cùng nhất.
3.  Trả về hàm bên trong.

---

## Learning Session Summary - 2025-01-04

### 🎯 Learning Objectives Achieved
- ✅ **Three-Level Currying Mastery**: `create_markdown_image(alt_text)(url)(title)` pattern
- ✅ **URL Encoding Implementation**: Parentheses → %28, %29 conversion
- ✅ **Optional Parameter Handling**: `title=None` with conditional logic
- ✅ **Real-World Application**: Markdown image syntax for Doc2Doc system

### 🏆 Test Results: **PERFECT 4/4 TESTS PASSED**
1. **Seal with title**: `![seal](https://imgur.com/oglPAXK "this is a seal")` ✅
2. **Cinnamon roll with title**: Complex alt-text handling ✅  
3. **Banana no title**: Optional parameter logic working ✅
4. **Wikipedia URL**: URL encoding of parentheses perfect ✅

### 💡 Student Implementation (Innovative Approach)
```python
def create_markdown_image(alt_text):
    square_bracket_alt_text = "![" + alt_text + "]"

    def inner_func(url):
        replace_url_1 = url.replace("(", "%28")
        replace_url_2 = replace_url_1.replace(")", "%29")
        alt_text_url = square_bracket_alt_text + f"({replace_url_2})"

        def inner_most_func(title=None):
            if not title is None:
                return alt_text_url.replace(")", f' "{title}")')
            else:
                return alt_text_url

        return inner_most_func

    return inner_func
```

**Key Innovation**: Using `.replace(")", f' "{title}")')` to transform base format rather than rebuilding strings.

### 🔄 Alternative Implementations Compared

#### Gemini's Approach (Explicit Rebuilding):
```python
def innermost_func(title=None):
    if title:
        return f"{square_bracket_alt_text}({escaped_url} \"{title}\")"
    return base_image_syntax
```

#### Claude's Approach (Clear Structure):
```python
def handle_title(title=None):
    if title is None:
        return f"{formatted_alt}({encoded_url})"
    else:
        return f"{formatted_alt}({encoded_url} \"{title}\")"
```

### 📊 Implementation Analysis

| Aspect | **Student** | **Claude** | **Gemini** |
|--------|-------------|------------|------------|
| **Efficiency** | ⭐⭐⭐ Best | ⭐⭐ Good | ⭐⭐ Good |
| **Innovation** | ⭐⭐⭐ Most creative | ⭐ Standard | ⭐ Standard |
| **Readability** | ⭐⭐ Complex | ⭐⭐⭐ Clear | ⭐⭐⭐ Clear |
| **Maintainability** | ⭐⭐ Advanced | ⭐⭐⭐ Easy | ⭐⭐⭐ Easy |

### 🌟 Key Learning Insights

#### Advanced Problem-Solving Demonstrated:
- **Systems Thinking**: Build base format once, modify as needed
- **Pattern Recognition**: Identified that only the ending differs between cases
- **Creative Solutions**: `.replace()` technique beyond conventional string building
- **Optimization Mindset**: Avoiding redundant string construction

#### Currying Evolution Mastery:
- **CH7-L1**: Two-parameter currying (font sizing) ✅
- **CH7-L4**: Three-parameter currying (document analysis) ✅  
- **CH7-L5**: Advanced three-parameter + URL encoding + optional params ✅

#### Vietnamese Technical Terms Mastered:
- **Ba cấp độ currying**: Three-level currying structure
- **Mã hóa URL**: URL encoding for special characters
- **Tham số tùy chọn**: Optional parameters with default values
- **Xử lý chuỗi điều kiện**: Conditional string manipulation

### 🎓 Professional Development Insights

**Student's approach demonstrates**:
- Advanced programming intuition beyond textbook solutions
- Efficiency-focused thinking (DRY principle application)
- Creative problem-solving that experienced developers often miss
- Understanding of string manipulation optimization techniques

**Pattern Recognition Excellence**: Successfully identified this as a "build base + conditionally modify" problem rather than "build different strings" problem.

### 🚀 Next Learning Opportunities
- **Function Composition**: Combining currying with map/filter/reduce
- **Partial Application**: Advanced currying patterns for API design
- **Performance Analysis**: Measuring efficiency gains in real applications
- **Code Review Skills**: Evaluating different solution approaches systematically

**Vietnamese Summary**: *Lesson này thể hiện sự tiến bộ vượt bậc trong tư duy lập trình. Cách tiếp cận sáng tạo cho thấy khả năng giải quyết vấn đề nâng cao và hiểu biết sâu về currying patterns.*
