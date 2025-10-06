# Ternary Expressions

[Ternaries](https://book.pythontips.com/en/latest/ternary%5Foperators.html) are a great way to reduce a series of statements, like an `if`/`else` block, to a single expression.

When you first learned how to use conditional logic in Python, it probably looked like this:

```py
result = 0
if number % 2 == 0:
    result = number / 2
else:
    result = (number * 3) + 1

```

This code sets `result` to a dummy value like `0` (`None` would also work), then overwrites it with its "real" value based on the condition.

A ternary lets us do all that in one expression:

```py
result = number / 2 if number % 2 == 0 else (number * 3) + 1

```

Note that we also avoided mutating the `result` variable. Ternary expressions are good for maintaining immutability.

The syntax for a ternary in Python is:

```py
value_a if condition else value_b

```

This qualifies as an _expression_ because it's a single statement that _evaluates to a value_ – one of two values, depending on the condition.

## When to Use Ternaries

Ternary expressions are cool, but _don't overdo it_. If you're dealing with complex conditional logic, it's often easier to work with full `if`/`else` blocks than to try to nest ternaries inside each other.

```py
msg = (
    "Access granted"
    if (
        user.is_authenticated
        and (user.role == "admin" or (user.role == "editor" and not user.suspended))
    )
    else ("Access limited" if user.is_authenticated else "Access denied")
)

```

## Assignment

Our Doc2Doc utility is designed to accept input documents in a variety of formats. It chooses the appropriate parser for a document based on the extension of the file name. Currently, only Markdown and plain-text parsers are supported.

**Fix the `choose_parser` function.** The logic is correct, but we want to simplify the conditional block to a one-line ternary expression.
---
## Gemini Translation (Bản Dịch Gemini)

# Biểu thức Tam phân (Ternary Expressions)

[Toán tử tam phân (Ternaries)](https://book.pythontips.com/en/latest/ternary%5Foperators.html) là một cách tuyệt vời để rút gọn một chuỗi các câu lệnh, như một khối `if`/`else`, thành một biểu thức duy nhất.

Khi bạn lần đầu học cách sử dụng logic điều kiện trong Python, có lẽ nó trông như thế này:

```py
result = 0
if number % 2 == 0:
    result = number / 2
else:
    result = (number * 3) + 1
```

Đoạn mã này đặt `result` thành một giá trị giả (dummy) như `0` (`None` cũng dùng được), sau đó ghi đè lên nó bằng giá trị "thực" của nó dựa trên điều kiện.

Một biểu thức tam phân cho phép chúng ta làm tất cả những điều đó trong một biểu thức duy nhất:

```py
result = number / 2 if number % 2 == 0 else (number * 3) + 1
```

Lưu ý rằng chúng ta cũng đã tránh được việc làm biến đổi (mutating) biến `result`. Biểu thức tam phân rất tốt cho việc duy trì tính bất biến (immutability).

Cú pháp cho một biểu thức tam phân trong Python là:

```py
value_a if condition else value_b
```

Điều này được coi là một _biểu thức_ bởi vì nó là một câu lệnh duy nhất _tính toán và trả về một giá trị_ – một trong hai giá trị, tùy thuộc vào điều kiện.

## Khi nào nên dùng Toán tử Tam phân

Biểu thức tam phân rất hay, nhưng _đừng lạm dụng nó_. Nếu bạn đang xử lý logic điều kiện phức tạp, việc sử dụng các khối `if`/`else` đầy đủ thường sẽ dễ dàng hơn là cố gắng lồng các biểu thức tam phân vào nhau.

```py
msg = (
    "Access granted"
    if (
        user.is_authenticated
        and (user.role == "admin" or (user.role == "editor" and not user.suspended))
    )
    else ("Access limited" if user.is_authenticated else "Access denied")
)
```

## Bài tập

Tiện ích Doc2Doc của chúng ta được thiết kế để chấp nhận các tài liệu đầu vào ở nhiều định dạng khác nhau. Nó chọn trình phân tích (parser) thích hợp cho một tài liệu dựa trên phần mở rộng của tên tệp. Hiện tại, chỉ có các trình phân tích Markdown và văn bản thuần túy (plain-text) được hỗ trợ.

**Hãy sửa hàm `choose_parser`.** Logic đã đúng, nhưng chúng tôi muốn đơn giản hóa khối điều kiện thành một biểu thức tam phân trên một dòng.

---
## Kế hoạch Học tập Nâng cao (Enhanced Learning Plan)

**1. Mục tiêu chính:**
Làm chủ các khái niệm Lập trình Hàm (FP) nền tảng và hiểu rõ cách chúng góp phần xây dựng các hệ thống AI đáng tin cậy, dễ dự đoán và dễ bảo trì.
*Lưu ý: Trong quá trình học, cân nhắc tích hợp các 'dự án AI nhỏ' để kết hợp nhiều khái niệm đã học vào các thành phần agent thực tế.*

**2. Phương pháp thực hiện (cho các bài học tới):**

*   **Bước 1: Phân tích bài tập & Kiểm thử trước (Test-First)**
    *   Với mỗi bài học, chúng ta sẽ bắt đầu bằng việc đọc và phân tích tệp `main_test.py` để hiểu rõ các yêu cầu và trường hợp biên.
    *   Chạy kiểm thử ngay từ đầu để thấy chúng thất bại. Đây là bước quan trọng trong quy trình Phát triển Hướng kiểm thử (TDD).

*   **Bước 2: Giải quyết bài toán (Implementation)**
    *   Áp dụng khái niệm vừa học để giải quyết bài tập trong `main.py`.
    *   Tôi sẽ tiếp tục sử dụng phương pháp Socratic, đặt câu hỏi gợi mở để anh tự đưa ra giải pháp.

*   **Bước 3: Kiểm thử và Hoàn thiện (Test & Refactor)**
    *   Chạy lại các bài kiểm thử cho đến khi tất cả đều thành công.
    *   Cùng nhau xem xét lại code để đảm bảo nó sạch, dễ đọc và tuân thủ các nguyên tắc FP.

*   **Bước 4: Kết nối với AI (Bridge to AI)**
    *   Sau khi giải quyết bài tập, chúng ta sẽ dành thời gian thảo luận: *"Khái niệm FP này giúp ích gì trong việc xây dựng một AI Agent? Nó làm cho agent tốt hơn ở điểm nào?"*

**3. Quy tắc Hợp tác (Collaboration Protocol):**
*   **Gemini (tôi):** Sẽ tập trung vào việc giải thích các khái niệm chuyên sâu bằng tiếng Việt, hướng dẫn bằng phương pháp Socratic và các nhiệm vụ đòi hỏi suy luận phức tạp.
*   **Claude:** Sẽ hỗ trợ các quy trình có cấu trúc như review code, thực hiện các thao tác với Git, hoặc các tác vụ được định nghĩa rõ ràng.

**4. Tiêu chí Thành công (Success Metrics):**
*   Với mỗi bài học, "làm chủ" được định nghĩa là: **vượt qua tất cả các bài kiểm thử VÀ có thể giải thích rõ ràng sự liên quan của khái niệm tới việc xây dựng AI Agent.**