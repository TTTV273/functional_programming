# Pure Functions

If you take nothing else away from this course, *please* take this: **[Pure functions](https://en.wikipedia.org/wiki/Pure_function) are fantastic.** They have two properties:

- They *always* return the same value given the same arguments.
- Running them causes no side effects

In short: **pure functions don't do anything with anything that exists outside of their scope.**

## Example of a Pure Function

```python
def find_max(nums):
    max_val = float("-inf")
    for num in nums:
        if max_val < num:
            max_val = num
    return max_val
```

## Example of an Impure Function

```python
# instead of returning a value
# this function modifies a global variable
global_max = float("-inf")

def find_max(nums):
    global global_max
    for num in nums:
        if global_max < num:
            global_max = num
```

## Assignment

There's a bug in the `convert_file_format` function! Right now, it relies on data outside its own scope. These global values can be changed by other parts of the code, so they are not guaranteed to be the same every time `convert_file_format` is called.

Fix the bug by making `convert_file_format` a pure function. It should only depend on data that is scoped inside of the function.

## Gemini Translation

### **# Hàm Thuần Khiết (Pure Functions)**

Nếu bạn không thể nhớ được gì khác từ khóa học này, thì *làm ơn* hãy nhớ điều này: **[Hàm thuần khiết](https://en.wikipedia.org/wiki/Pure_function) thật sự rất tuyệt vời.** Chúng có hai đặc tính cốt lõi:

1. Chúng **luôn luôn** trả về cùng một kết quả nếu nhận cùng các đối số đầu vào.
2. Việc thực thi chúng **không gây ra bất kỳ tác dụng phụ (side effect)** nào.

Nói một cách ngắn gọn: **hàm thuần khiết không tương tác với bất cứ thứ gì tồn tại bên ngoài phạm vi (scope) của chính nó.**

-----

### **## Ví dụ về Hàm Thuần Khiết**

```python
def find_max(nums):
    # Khởi tạo giá trị lớn nhất là số âm vô cùng
    max_val = float("-inf")
    # Lặp qua từng số trong danh sách
    for num in nums:
        # Nếu tìm thấy số lớn hơn, cập nhật max_val
        if max_val < num:
            max_val = num
    # Trả về giá trị lớn nhất tìm được
    return max_val
```

Hàm `find_max` này là thuần khiết vì nó chỉ phụ thuộc vào danh sách `nums` được truyền vào và luôn trả về một giá trị, không làm thay đổi bất cứ thứ gì bên ngoài.

-----

### **## Ví dụ về Hàm Không Thuần Khiết (Impure Function)**

```python
# Thay vì trả về một giá trị,
# hàm này lại sửa đổi một biến toàn cục (global variable).
global_max = float("-inf")

def find_max(nums):
    # Khai báo rằng chúng ta sẽ sử dụng biến toàn cục
    global global_max
    # Lặp qua từng số
    for num in nums:
        # Sửa đổi trực tiếp biến toàn cục
        if global_max < num:
            global_max = num
```

Hàm này **không thuần khiết** vì nó có "tác dụng phụ": nó làm thay đổi giá trị của biến `global_max`, một biến nằm ngoài phạm vi của hàm.

-----

### **## Bài Tập**

Có một lỗi (bug) trong hàm `convert_file_format`! Hiện tại, nó đang phụ thuộc vào dữ liệu bên ngoài phạm vi của chính nó. Các giá trị toàn cục này có thể bị thay đổi bởi các phần khác của mã, vì vậy chúng không được đảm bảo sẽ giữ nguyên mỗi khi hàm `convert_file_format` được gọi.

**Nhiệm vụ của bạn là sửa lỗi này bằng cách biến `convert_file_format` thành một hàm thuần khiết.** Nó chỉ nên phụ thuộc vào dữ liệu được định nghĩa bên trong phạm vi của chính hàm đó.