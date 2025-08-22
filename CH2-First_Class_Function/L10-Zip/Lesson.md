# Zip

The [zip](https://docs.python.org/3/library/functions.html#zip) function takes two iterables (in this case lists), and returns a *new* iterable where each element is a tuple containing one element from each of the original iterables.

```python
a = [1, 2, 3]
b = [4, 5, 6]

c = list(zip(a, b))
print(c)
# [(1, 4), (2, 5), (3, 6)]
```

## Assignment

Complete the `pair_document_with_format` function. It takes two lists of strings as input:

- `doc_names`: the names of documents
- `doc_formats`: the file formats of the documents

1. `zip` up the lists into a single list of tuples with the names as the first index and the formats as the second index in each tuple.
2. [filter](https://docs.python.org/3/library/functions.html#filter) the list of tuples to only include tuples where the format is one of the given `valid_formats`.

Return the result **as a list**.

## Key Learning Points

### Zip Function Concept
- **Purpose**: Combines multiple iterables element-wise into tuples
- **Pattern**: `zip(list1, list2)` → `[(item1_a, item1_b), (item2_a, item2_b), ...]`
- **Memory Efficient**: Returns iterator, use `list()` to convert when needed
- **Length Handling**: Stops at shortest iterable length

### Practical Applications
- **Document Processing**: Pairing filenames with formats, metadata, or properties
- **Data Correlation**: Connecting related data from separate sources
- **Parallel Processing**: Processing corresponding elements from multiple lists
- **Matrix Operations**: Working with coordinate pairs or data relationships

### Function Composition with Zip
- **Zip + Filter**: Combine data then filter based on criteria
- **Zip + Map**: Transform paired data with functions
- **Pipeline Pattern**: `list(filter(condition, zip(list1, list2)))`

### Common Use Cases
- **File Management**: Matching filenames with extensions or metadata
- **Data Validation**: Checking correspondence between parallel datasets
- **Coordinate Processing**: Working with (x, y) pairs or geographic data
- **Configuration Mapping**: Pairing keys with values for dynamic setup

## Gemini Translation

# Hàm Zip

Hàm [zip](https://docs.python.org/3/library/functions.html#zip) nhận vào hai đối tượng có thể lặp (trong trường hợp này là danh sách) và trả về một đối tượng lặp *mới*, trong đó mỗi phần tử là một tuple chứa một phần tử từ mỗi đối tượng lặp ban đầu.

```python
a = [1, 2, 3]
b = [4, 5, 6]

c = list(zip(a, b))
print(c)
# Kết quả: [(1, 4), (2, 5), (3, 6)]
```

## Bài tập

Hoàn thành hàm `pair_document_with_format`. Hàm này nhận vào hai danh sách chuỗi:

  - `doc_names`: tên của các tài liệu
  - `doc_formats`: định dạng tệp của các tài liệu

<!-- end list -->

1.  Sử dụng hàm `zip` để gộp các danh sách thành một danh sách duy nhất chứa các tuple, với tên tệp ở vị trí đầu tiên và định dạng ở vị trí thứ hai trong mỗi tuple.
2.  Sử dụng hàm [filter](https://docs.python.org/3/library/functions.html#filter) để lọc danh sách các tuple, chỉ giữ lại những tuple có định dạng tệp nằm trong danh sách `valid_formats` cho trước.

Trả về kết quả **dưới dạng một danh sách (list)**.

## Những điểm chính cần học

### Khái niệm về hàm Zip

  - **Mục đích**: Kết hợp nhiều đối tượng lặp theo từng phần tử vào các tuple.
  - **Cấu trúc**: `zip(list1, list2)` → `[(item1_a, item1_b), (item2_a, item2_b), ...]`
  - **Hiệu quả về bộ nhớ**: Trả về một iterator, sử dụng `list()` để chuyển đổi khi cần.
  - **Xử lý độ dài**: Dừng lại ở độ dài của đối tượng lặp ngắn nhất.

### Ứng dụng thực tế

  - **Xử lý tài liệu**: Ghép cặp tên tệp với định dạng, siêu dữ liệu hoặc thuộc tính.
  - **Tương quan dữ liệu**: Kết nối các dữ liệu liên quan từ các nguồn riêng biệt.
  - **Xử lý song song**: Xử lý các phần tử tương ứng từ nhiều danh sách.
  - **Thao tác ma trận**: Làm việc với các cặp tọa độ hoặc các mối quan hệ dữ liệu.

### Kết hợp hàm (Function Composition) với Zip

  - **Zip + Filter**: Kết hợp dữ liệu rồi lọc dựa trên tiêu chí.
  - **Zip + Map**: Biến đổi dữ liệu đã được ghép cặp bằng các hàm.
  - **Mô hình xử lý chuỗi (Pipeline Pattern)**: `list(filter(condition, zip(list1, list2)))`

### Các trường hợp sử dụng phổ biến

  - **Quản lý tệp**: Khớp tên tệp với phần mở rộng hoặc siêu dữ liệu.
  - **Xác thực dữ liệu**: Kiểm tra sự tương ứng giữa các tập dữ liệu song song.
  - **Xử lý tọa độ**: Làm việc với các cặp (x, y) hoặc dữ liệu địa lý.
  - **Ánh xạ cấu hình**: Ghép cặp các khóa (key) với giá trị (value) để thiết lập động.