# Why Python?

1. **No static typing (Không có kiểu tĩnh)**
    - **Giải thích:** Trong Python, anh có thể tạo một biến `x = 10` (số nguyên) rồi ngay sau đó gán `x = "hello"` (chuỗi). Python chỉ kiểm tra kiểu dữ liệu **khi chạy code**. Ngược lại, các ngôn ngữ FP "thuần túy" thường có "kiểu tĩnh", nghĩa là ta phải định nghĩa kiểu dữ liệu ngay từ đầu (`int x = 10`) và không thể thay đổi nó.
    - **Điểm yếu cho FP:** FP ưa thích sự chặt chẽ và có thể dự đoán. "Kiểu tĩnh" giống như một hợp đồng, đảm bảo một hàm luôn nhận đúng loại đầu vào và trả về đúng loại đầu ra, giúp phát hiện lỗi ngay từ lúc viết code.

2. **(Almost) everything is mutable (Hầu hết mọi thứ đều có thể thay đổi)**
    - **Giải thích:** Như chúng ta đã thảo luận, các đối tượng trong Python như `list` hay `dictionary` có thể bị thay đổi sau khi tạo ra.
    - **Điểm yếu cho FP:** Triết lý của FP là **tính bất biến (immutability)**. Thay vì thay đổi dữ liệu, bạn tạo ra dữ liệu mới. Điều này tránh các lỗi không mong muốn và làm cho chương trình dễ dự đoán hơn.

1. **No tail call optimization (Không tối ưu hóa cho cuộc gọi đuôi)**

    - **Giải thích:** Đây là một kỹ thuật tối ưu hóa cho **đệ quy** (recursion) - khi một hàm tự gọi lại chính nó. Trong Python, mỗi lần một hàm tự gọi lại, nó sẽ chiếm thêm một phần bộ nhớ (call stack). Nếu gọi quá nhiều lần, nó sẽ gây tràn bộ nhớ (stack overflow).

    - **Điểm yếu cho FP:** FP sử dụng đệ quy rất nhiều. Các ngôn ngữ FP có "tối ưu hóa cuộc gọi đuôi", cho phép đệ quy chạy vô hạn mà không làm tràn bộ nhớ. Việc Python không có tính năng này làm cho việc sử dụng đệ quy theo phong cách FP bị hạn chế.

1. **Side effects are common (Tác dụng phụ là phổ biến)**

    - **Giải thích:** Một hàm có "tác dụng phụ" khi nó làm một việc gì đó bên ngoài phạm vi của nó, thay vì chỉ nhận đầu vào và trả về kết quả. Ví dụ: thay đổi một biến toàn cục, in ra màn hình, ghi vào một file.

    - **Điểm yếu cho FP:** Đề cao các **các hàm thuần túy (pure functions)**, tức là những hàm không có tác dụng phụ. Điều này làm cho chúng dễ kiểm thử và có thể dự đoán 100%.

1. **Imperative and OOP style abound (Phong cách Mệnh lệnh và Hướng đối tượng chiếm ưu thế)**

    - **Giải thích:** Hầu hết các thư viện phổ biến của Python (Pandas, Numpy,...) được thiết kế theo phong cách Hướng đối tượng (OOP) hoặc Mệnh lệnh. Ví dụ, `my_list.sort()` là một phương thức thay đổi chính `my_list`.

    - **Điểm yếu cho FP:** Điều này khiến việc viết code theo phong cách FP trong Python đôi khi không được tự nhiên. thay vì `my_list.sort()`, một thư viện FP sẽ cung cấp một hàm như `sorted_list = sort(my_list)`.

1. **Purity is not enforced (Tính thuần túy không bị bắt buộc)**

    - **Giải thích:** Đây là hệ quả của các điểm trên. Ngôn ngữ Python không có cơ chế nào "ép" anh phải viết các hàm thuần túy. Việc này phụ thuộc hoàn toàn vào kỷ luật của người lập trình.

    - **Điểm yếu cho FP:** Các ngôn ngữ FP thuần túy như Haskell gây khó khăn cho việc tạo ra các tác dụng phụ, do đó đảm bảo code tuân thủ các nguyên tắc của FP một cách chặt chẽ hơn.

1. **Sum Types are hard to define (Khó định nghĩa Sum Types)**

    - **Giải thích:** "Sum Types" là một kiểu dữ liệu có thể là một trong nhiều loại khác nhau. Ví dụ, một biến `Kết quả` có thể là `Thành công(dữ_liệu)` hoặc là `Thất bại(lỗi)`.

    - **Điểm yếu cho FP:** Các ngôn ngữ FP có hỗ trợ mạnh mẽ cho Sum Types, giúp xử lý các trường hợp khác nhau một cách an toàn và rõ ràng. Trong Python, chúng ta thường phải dùng các cấu trúc `if/else` để kiểm tra kiểu, vốn không thanh lịch bằng.

1. **Pattern matching is weak as best (Đối sánh mẫu còn yếu)**

    - **Giải thích:** "Pattern Matching" là một cấu trúc điều khiển mạnh mẽ, giống như `if/else` phiên bản "cao cấp". Nó cho phép bạn kiểm tra "hình dạng" của dữ liệu và lấy ra các phần tử bạn muốn một cách gọn gàng. Python 3.10 đã giới thiệu `match/case`, nhưng nó vẫn còn hạn chế so với các ngôn ngữ FP.

    - **Điểm yếu cho FP:** Trong các ngôn ngữ FP, "Pattern Matching" được sử dụng rộng rãi cùng với "Sum Types" để tạo ra code rất dễ đọc và mạnh mẽ.
