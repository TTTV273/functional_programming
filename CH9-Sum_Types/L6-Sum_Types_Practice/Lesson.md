# Sum Types Practice

Doc2Doc should be able to prepare and export a CSV file of whatever data you input. Comma-Separated Values are a ubiquitous text format that allows for information to be structured in a table. There is usually a header row, followed by data rows. Within rows, items are separated by commas.

## Assignment

Complete the `get_csv_status` function. It should use a match case statement to select the correct response depending on the status of the export operation. Create functions to handle each operation as follows:

1. `PENDING`: return a tuple with the string `"Pending..."` and the data converted from a list of lists of anything, to a list of lists of strings.
   1. Try to use nested map functions to convert the data items into strings.
   2. Remember to convert from a map object back into a list.

2. `PROCESSING`: return a tuple with the string `"Processing..."` and the data converted from a list of lists of strings into one string in CSV format.
   1. For each list of strings, combine the strings with `join` with commas inbetween to form a row.
   2. For each row string, combine the strings with `join` with newlines `"\n"` inbetween to form a table.

3. `SUCCESS`: return a tuple with the string `"Success!"` and simply return the data as is.

4. `FAILURE`: return a tuple with the string `"Unknown error, retrying..."` and the data after it has been prepared and processed into a CSV string, by combining the steps for `Pending` and `Processing`.

5. Any Other Status: raise an `Exception` with the string `"unknown export status"`.

## Tip

It's better if you try this challenge without using loops for practice, but you may use loops.

## Gemini Translation

Tất nhiên rồi, đây là nội dung bài học được dịch sang tiếng Việt.

---

### Thực hành về Sum Types

Doc2Doc cần có khả năng chuẩn bị và xuất tệp CSV từ bất kỳ dữ liệu nào bạn nhập vào. **Giá trị được phân tách bằng dấu phẩy** (CSV) là một định dạng văn bản phổ biến cho phép cấu trúc thông tin thành dạng bảng. Thường sẽ có một hàng tiêu đề, theo sau là các hàng dữ liệu. Trong mỗi hàng, các mục được phân tách bằng dấu phẩy.

### Bài tập

Hoàn thành hàm `get_csv_status`. Hàm này nên sử dụng lệnh `match case` để chọn phản hồi chính xác tùy thuộc vào trạng thái của hoạt động xuất file. Hãy tạo các hàm để xử lý từng hoạt động như sau:

1. `PENDING` (Đang chờ): trả về một tuple với chuỗi `"Pending..."` và dữ liệu được chuyển đổi từ một danh sách các danh sách (list of lists) chứa bất kỳ thứ gì, thành một danh sách các danh sách chuỗi.
   1. Hãy thử sử dụng các hàm `map` lồng nhau để chuyển đổi các mục dữ liệu thành chuỗi.
   2. Nhớ chuyển đổi từ đối tượng `map` trở lại thành `list`.

2. `PROCESSING` (Đang xử lý): trả về một tuple với chuỗi `"Processing..."` và dữ liệu được chuyển đổi từ một danh sách các danh sách chuỗi thành một chuỗi duy nhất ở định dạng CSV.
   1. Đối với mỗi danh sách chuỗi (tức là mỗi hàng), hãy kết hợp các chuỗi lại bằng hàm `join` với dấu phẩy ở giữa.
   2. Đối với mỗi chuỗi hàng, hãy kết hợp chúng lại bằng hàm `join` với ký tự xuống dòng `"\n"` ở giữa để tạo thành bảng.

3. `SUCCESS` (Thành công): trả về một tuple với chuỗi `"Success!"` và chỉ cần trả lại dữ liệu nguyên trạng.

4. `FAILURE` (Thất bại): trả về một tuple với chuỗi `"Unknown error, retrying..."` và dữ liệu sau khi đã được chuẩn bị và xử lý thành chuỗi CSV, bằng cách kết hợp các bước của `PENDING` và `PROCESSING`.

5. Bất kỳ trạng thái nào khác: ném ra một `Exception` với chuỗi `"unknown export status"`.

### Gợi ý

Tốt hơn là bạn nên thử thách này mà không sử dụng vòng lặp để luyện tập, nhưng bạn vẫn có thể sử dụng chúng.

---

Bài tập này khá phức tạp vì nó kết hợp nhiều bước xử lý dữ liệu. Để bắt đầu, chúng ta hãy tập trung vào trường hợp đầu tiên: `PENDING`.

Anh có muốn cùng em xem lại cách dùng hàm `map` để biến đổi một danh sách không?
