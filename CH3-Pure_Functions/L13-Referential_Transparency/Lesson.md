# Referential Transparency

Pure functions are always [referentially transparent](https://www.baeldung.com/cs/referential-transparency#referential-transparency).

"Referential transparency" is a fancy way of saying that a function call can be replaced by its would-be return value because it's the same every time. **Referentially transparent functions can be safely memoized.** For example `add(2, 3)` can be smartly replaced by the value `5`.

The great thing about pure functions is that they can always be *safely* memoized. Impure functions can't be because they might do something in addition to returning a static value, or they might return different values given the same arguments.

## Should I Always Memoize?

No! Memoization is a *tradeoff* between memory and speed. If your function is fast to execute, it's probably not worth memoizing, because the amount of RAM (memory) your program will need to store the results will go way up.

It's also a bunch of extra code to write, so you should only do it if you have a good reason to.

## Gemini Translation (Bản Dịch Gemini)

### **# Tính minh bạch tham chiếu (Referential Transparency)**

Các hàm thuần khiết (pure functions) luôn có [tính minh bạch tham chiếu](https://www.baeldung.com/cs/referential-transparency#referential-transparency).

"Tính minh bạch tham chiếu" là một cách nói mỹ miều rằng một lời gọi hàm có thể được thay thế bằng giá trị trả về của nó vì kết quả luôn luôn giống nhau. **Các hàm có tính minh bạch tham chiếu có thể được ghi nhớ hóa (memoized) một cách an toàn.** Ví dụ, `add(2, 3)` có thể được thay thế một cách thông minh bằng giá trị `5`.

Điều tuyệt vời về các hàm thuần khiết là chúng luôn có thể được ghi nhớ hóa một cách *an toàn*. Các hàm không thuần khiết (impure functions) thì không thể vì chúng có thể làm một điều gì đó khác ngoài việc trả về một giá trị tĩnh, hoặc chúng có thể trả về các giá trị khác nhau dù có cùng tham số đầu vào.

### **## Tôi có nên luôn luôn Memoize không?**

Không! Memoization là một sự *đánh đổi* giữa bộ nhớ và tốc độ. Nếu hàm của bạn thực thi nhanh, có lẽ nó không đáng để memoize, vì lượng RAM (bộ nhớ) mà chương trình của bạn cần để lưu trữ kết quả sẽ tăng lên rất nhiều.

Nó cũng đòi hỏi phải viết thêm một mớ code, vì vậy bạn chỉ nên làm điều đó khi có lý do chính đáng.

## Mối Liên Hệ với Hàm Thuần Khiết

- **Pure Functions = Referential Transparency**: Hàm thuần khiết đảm bảo tính minh bạch tham chiếu
- **Deterministic Behavior**: Cùng input → cùng output → có thể thay thế an toàn
- **Memoization Safety**: Chỉ hàm có tính minh bạch tham chiếu mới an toàn để cache
- **Mathematical Foundation**: Cơ sở lý thuyết cho các kỹ thuật tối ưu hóa functional programming