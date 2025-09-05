# Currying Practice

Doc2Doc should include a feature for image resizing, allowing users to adjust image dimensions to specified ranges. This ensures that images in documents fit and aren't freakishly large or hilariously small.

## Assignment

Complete the `new_resizer` function using currying. It should make sure the image dimensions are never smaller than the minimum width and height, or larger than the maximum width and height specified.

1. The `new_resizer` function takes integer inputs `max_width` and `max_height` and returns an inner function.
2. The inner function should take optional integer inputs `min_width` and `min_height`  with default values `0`  and return an innermost function.
   - If `min_width` is more than `max_width` or `min_height` is more than `max_height`, raise an exception `"minimum size cannot exceed maximum size"`.
3. The innermost function should take two integer inputs `width` and `height` and return two integers.
   - Use the built-in [`min`](https://docs.python.org/3/library/functions.html#min) and [`max`](https://docs.python.org/3/library/functions.html#max) functions to reduce or increase the `width` and `height` as needed, then return the new `width` and new `height`.

## Example

If our `new_resizer` function returns a `set_min_size` function, and `set_min_size` returns a `resize_image` function, we would use it like this:

```python
# Step 1: Create the resizer with maximum dimensions
set_min_size = new_resizer(800, 600)

# Step 2: Set the minimum dimensions
resize_image = set_min_size(200, 100)

# Step 3: Resize the image
new_width, new_height = resize_image(1000, 500)

# Step 4: Output the result
print(new_width, new_height)  # Output: 800, 500

# With currying syntax
print(new_resizer(800, 600)(200, 100)(1000, 500))  # Output: (800, 500)
```

## Gemini Translation

### Thực hành về Currying

Doc2Doc nên có một tính năng thay đổi kích thước ảnh, cho phép người dùng điều chỉnh kích thước ảnh theo một khoảng cho trước. Điều này đảm bảo ảnh trong tài liệu sẽ vừa vặn, không quá lớn hoặc quá nhỏ một cách bất thường.

### Yêu cầu

Hoàn thành hàm `new_resizer` bằng cách sử dụng kỹ thuật currying. Hàm này cần đảm bảo kích thước ảnh không bao giờ nhỏ hơn chiều rộng và chiều cao tối thiểu, hoặc lớn hơn chiều rộng và chiều cao tối đa đã chỉ định.

1.  Hàm `new_resizer` nhận vào hai số nguyên `max_width` và `max_height` và trả về một hàm bên trong.
2.  Hàm bên trong sẽ nhận vào hai số nguyên tùy chọn `min_width` và `min_height`—với giá trị mặc định là `0`—và trả về một hàm sâu nhất.
      * Nếu `min_width` lớn hơn `max_width` hoặc `min_height` lớn hơn `max_height`, hãy ném ra một ngoại lệ (exception) với thông báo `"minimum size cannot exceed maximum size"`.
3.  Hàm sâu nhất sẽ nhận vào hai số nguyên `width` và `height` và trả về hai số nguyên.
      * Sử dụng các hàm có sẵn là [`min`](https://docs.python.org/3/library/functions.html#min) và [`max`](https://docs.python.org/3/library/functions.html#max) để giảm hoặc tăng `width` và `height` khi cần, sau đó trả về `width` và `height` mới.

### Ví dụ

Nếu hàm `new_resizer` của chúng ta trả về một hàm `set_min_size`, và `set_min_size` trả về một hàm `resize_image`, chúng ta sẽ sử dụng nó như sau:

```python
# Bước 1: Tạo resizer với kích thước tối đa
set_min_size = new_resizer(800, 600)

# Bước 2: Thiết lập kích thước tối thiểu
resize_image = set_min_size(200, 100)

# Bước 3: Thay đổi kích thước ảnh
new_width, new_height = resize_image(1000, 500)

# Bước 4: In ra kết quả
print(new_width, new_height) # Output: 800, 500

# Với cú pháp currying
print(new_resizer(800, 600)(200, 100)(1000, 500)) # Output: (800, 500)
```