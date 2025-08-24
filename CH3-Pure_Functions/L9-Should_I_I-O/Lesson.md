# Should I I/O?

A program that doesn't do *any* i/o is pretty useless. What's the point of computing something if you can't see the results?

![Useless computation](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/LUg4s1f.jpeg)

In functional programming, i/o is viewed as *dirty* but *necessary*. We know we can't *eliminate* i/o from our code, so we just *contain* it as much as possible. There should be a clear place in your project that does nasty i/o stuff, and the rest of your code can be pure.

For example, a Python program might:

1. Read a file from the hard drive as the program starts
2. Run a bunch of pure functions to analyze the data
3. Write the results of the analysis to a file on the hard drive at the end

![I/O Sandwich Pattern](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/45emq7q-594x400.png)

## Gemini Translation (Bản Dịch Gemini)

### **# Tôi có nên thực hiện I/O không?**

Một chương trình không thực hiện *bất kỳ* hành động I/O nào thì khá là vô dụng. Ý nghĩa của việc tính toán một cái gì đó là gì nếu bạn không thể xem được kết quả?

*![Tính toán vô dụng](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/LUg4s1f.jpeg)*

Trong lập trình hàm, I/O được xem là ***"bẩn" (dirty)*** nhưng ***cần thiết (necessary)***. Chúng ta biết rằng chúng ta không thể *loại bỏ hoàn toàn* I/O khỏi code của mình, vì vậy chúng ta chỉ ***cô lập (contain)*** nó nhiều nhất có thể. Nên có một nơi rõ ràng trong dự án của bạn chuyên để thực hiện những công việc I/O "bẩn thỉu", và phần còn lại của code có thể giữ được sự trong sạch.

Ví dụ, một chương trình Python có thể:

1. Đọc một tập tin từ ổ cứng khi chương trình bắt đầu.
2. Chạy một loạt các hàm trong sạch để phân tích dữ liệu.
3. Ghi kết quả phân tích vào một tập tin trên ổ cứng ở cuối chương trình.

*![Mẫu I/O Sandwich](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/45emq7q-594x400.png)*

## Kiến Trúc "I/O Sandwich" (I/O Sandwich Architecture)

Đây là một mẫu thiết kế quan trọng trong lập trình hàm:

- **Lớp Đầu Vào (Input Layer)**: Thực hiện các hoạt động I/O "bẩn" để đọc dữ liệu
- **Lớp Xử Lý (Processing Layer)**: Sử dụng các hàm thuần khiết để xử lý dữ liệu  
- **Lớp Đầu Ra (Output Layer)**: Thực hiện các hoạt động I/O "bẩn" để ghi kết quả

**Lợi ích của mẫu này:**
- Code xử lý chính hoàn toàn thuần khiết và dễ kiểm thử
- I/O được cô lập ở các biên của chương trình
- Dễ bảo trì và gỡ lỗi vì logic và I/O được tách biệt rõ ràng