# Higher Order Functions Practice

Doc2Doc needs a way to restore documents from saved backups. However, not all original documents may have backups, and some backups might be corrupted.

## Assignment

Complete the `restore_documents` function in one line - if you can. It takes two tuples of document strings, `originals` and `backups`, as input and returns a `set`.

1. Convert all documents to the same case with `.upper()` for comparison.
2. Filter out documents that are corrupted strings of random numbers with `.isdigit()`.
3. Return the combined `originals` and `backups` tuples, removing any duplicates using a `set`.

## Tip

I used `map`, `filter` and lambda functions to complete the function on one line, but it's split up by multi-line formatting for your readability.

## Key Learning Points

### Higher-Order Function Composition
- **Chaining Operations**: Combine `map`, `filter`, and set operations in sequence
- **Multi-Step Processing**: Transform → Filter → Combine → Deduplicate
- **One-Line Implementation**: Complex logic expressed concisely through function composition
- **Readable Formatting**: Multi-line formatting maintains readability despite single expression

### Document Processing Pipeline
- **Case Normalization**: `.upper()` ensures consistent comparison across documents
- **Corruption Detection**: `.isdigit()` identifies corrupted files containing only numbers
- **Data Merging**: Combine multiple data sources (originals + backups)
- **Deduplication**: Set automatically removes duplicate documents

### Advanced Functional Patterns
- **Tuple Concatenation**: Merging multiple iterables before processing
- **Predicate Composition**: Complex filtering with multiple conditions
- **Iterator Chaining**: Seamless flow from transformation to filtering to collection
- **Type Conversion**: Strategic use of `set()` for both deduplication and result type

### Real-World Applications
- **Backup Systems**: Document restoration with integrity checking
- **Data Cleaning**: Remove corrupted or invalid entries from datasets
- **File Management**: Merge and deduplicate file collections
- **Content Processing**: Normalize and validate text data

### Performance Considerations
- **Memory Efficiency**: Iterator-based processing until final collection
- **Set Operations**: O(1) average case for deduplication and membership testing
- **Lazy Evaluation**: Transformations applied only when needed
- **Single Pass**: All operations combined into one traversal where possible

### Business Logic Integration
- **Data Validation**: Automated detection of corrupted files
- **Consistency**: Case-insensitive document matching
- **Reliability**: Robust handling of mixed data sources
- **Scalability**: Pattern works for any number of document sources

## Gemini Translation

# Thực hành về Hàm bậc cao

Doc2Doc cần một cách để khôi phục tài liệu từ các bản sao lưu đã lưu. Tuy nhiên, không phải tất cả tài liệu gốc đều có bản sao lưu, và một số bản sao lưu có thể bị hỏng.

## Bài tập

Hoàn thành hàm `restore_documents` trong một dòng - nếu bạn có thể. Hàm này nhận vào hai tuple chứa các chuỗi tài liệu, `originals` và `backups`, và trả về một `set` (tập hợp).

1.  Chuyển đổi tất cả tài liệu về cùng một kiểu chữ (in hoa) bằng `.upper()` để so sánh.
2.  Lọc ra những tài liệu là chuỗi số ngẫu nhiên bị hỏng bằng `.isdigit()`.
3.  Trả về một `set` kết hợp cả `originals` và `backups`, loại bỏ bất kỳ bản sao nào bị trùng lặp.

## Gợi ý

Tôi đã sử dụng các hàm `map`, `filter` và lambda để hoàn thành hàm này trên một dòng, nhưng nó được tách ra thành nhiều dòng để bạn dễ đọc hơn.

## Những điểm chính cần học

### Kết hợp các Hàm bậc cao (Higher-Order Function Composition)
- **Nối chuỗi các thao tác**: Kết hợp `map`, `filter`, và các thao tác với `set` theo một chuỗi.
- **Xử lý đa bước**: Biến đổi → Lọc → Kết hợp → Loại bỏ trùng lặp.
- **Triển khai trong một dòng**: Logic phức tạp được diễn đạt ngắn gọn thông qua việc kết hợp hàm.
- **Định dạng dễ đọc**: Định dạng nhiều dòng giúp duy trì khả năng đọc dù chỉ là một biểu thức duy nhất.

### Quy trình xử lý tài liệu (Pipeline)
- **Chuẩn hóa kiểu chữ**: `.upper()` đảm bảo so sánh nhất quán giữa các tài liệu.
- **Phát hiện hỏng hóc**: `.isdigit()` xác định các tệp bị hỏng chỉ chứa số.
- **Gộp dữ liệu**: Kết hợp nhiều nguồn dữ liệu (gốc + sao lưu).
- **Loại bỏ trùng lặp**: `set` tự động loại bỏ các tài liệu trùng lặp.

### Các mẫu Lập trình hàm nâng cao
- **Nối Tuple**: Gộp nhiều đối tượng lặp trước khi xử lý.
- **Kết hợp các vị từ (Predicate Composition)**: Lọc phức tạp với nhiều điều kiện.
- **Nối chuỗi các Iterator**: Luồng xử lý liền mạch từ biến đổi đến lọc và thu thập.
- **Chuyển đổi kiểu**: Sử dụng `set()` một cách có chiến lược cho cả việc loại bỏ trùng lặp và xác định kiểu dữ liệu trả về.

### Ứng dụng thực tế
- **Hệ thống sao lưu**: Khôi phục tài liệu với việc kiểm tra tính toàn vẹn.
- **Làm sạch dữ liệu**: Loại bỏ các mục bị hỏng hoặc không hợp lệ khỏi tập dữ liệu.
- **Quản lý tệp**: Gộp và loại bỏ trùng lặp trong các bộ sưu tập tệp.
- **Xử lý nội dung**: Chuẩn hóa và xác thực dữ liệu văn bản.

### Cân nhắc về hiệu suất
- **Hiệu quả bộ nhớ**: Xử lý dựa trên iterator cho đến bước thu thập cuối cùng.
- **Thao tác với Set**: Độ phức tạp O(1) trong trường hợp trung bình cho việc loại bỏ trùng lặp và kiểm tra thành viên.
- **Đánh giá lười (Lazy Evaluation)**: Các phép biến đổi chỉ được áp dụng khi cần thiết.
- **Một lần duyệt**: Tất cả các thao tác được kết hợp thành một lần duyệt qua dữ liệu nếu có thể.

### Tích hợp Logic nghiệp vụ
- **Xác thực dữ liệu**: Tự động phát hiện các tệp bị hỏng.
- **Tính nhất quán**: So khớp tài liệu không phân biệt chữ hoa chữ thường.
- **Độ tin cậy**: Xử lý mạnh mẽ các nguồn dữ liệu hỗn hợp.
- **Khả năng mở rộng**: Mô hình hoạt động cho bất kỳ số lượng nguồn tài liệu nào.