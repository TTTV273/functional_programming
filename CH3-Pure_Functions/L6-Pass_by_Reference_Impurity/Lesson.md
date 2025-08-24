# Pass by Reference Impurity

Because certain types in Python are passed by reference, we can mutate values that we didn't intend to. This is a form of function impurity.

Remember, a pure function should have *no side effects*. It shouldn't modify anything outside of its scope, *including its inputs*. It should return new copies of inputs instead of changing them.

## Pure Function

```python
def remove_format(default_formats, old_format):
    new_formats = default_formats.copy()
    new_formats[old_format] = False
    return new_formats
```

## Impure Function

```python
def remove_format(default_formats, old_format):
    default_formats[old_format] = False
    return default_formats
```

## Why Do We Care?

One of the biggest differences between good and great developers is how often they incorporate pure functions into their code. Pure functions are easier to read, easier to reason about, easier to test, and easier to combine. Even if you're working in an imperative language like Python, you can (and should) write pure functions whenever reasonable.

There's nothing worse than trying to debug a program where the order of function calls needs to be *juuuuust right* because they all read and modify the same global variable.

## Gemini Translation

### **# Sự "Không Trong Sạch" do Truyền Bằng Tham Chiếu (Pass by Reference Impurity)**

Bởi vì một số kiểu dữ liệu nhất định trong Python được truyền bằng tham chiếu (passed by reference), chúng ta có thể làm thay đổi các giá trị mà chúng ta không hề có ý định. Đây là một dạng "không trong sạch" của hàm.

Hãy nhớ rằng, một **hàm trong sạch (pure function)** phải ***không có tác dụng phụ (side effects)***. Nó không được phép sửa đổi bất cứ thứ gì bên ngoài phạm vi của nó, ***kể cả các giá trị đầu vào***. Thay vào đó, nó nên trả về một bản sao mới của các giá trị đầu vào.

### **## Hàm Trong Sạch (Pure Function)**

```python
def remove_format(default_formats, old_format):
    # Tạo một bản sao mới để không làm thay đổi bản gốc
    new_formats = default_formats.copy()
    
    # Thay đổi trên bản sao
    new_formats[old_format] = False
    
    # Trả về bản sao đã thay đổi
    return new_formats
```

### **## Hàm Không Trong Sạch (Impure Function)**

```python
def remove_format(default_formats, old_format):
    # Thay đổi trực tiếp trên giá trị đầu vào ban đầu
    default_formats[old_format] = False
    
    # Trả về giá trị đầu vào đã bị thay đổi
    return default_formats
```

### **## Tại Sao Chúng Ta Cần Quan Tâm?**

Một trong những khác biệt lớn nhất giữa một lập trình viên giỏi và một lập trình viên xuất sắc là tần suất họ sử dụng các hàm trong sạch trong code của mình. Các hàm trong sạch **dễ đọc hơn, dễ suy luận hơn, dễ kiểm thử (test) hơn, và dễ kết hợp** với nhau hơn. Ngay cả khi bạn đang làm việc với một ngôn ngữ lập trình mệnh lệnh (imperative) như Python, bạn vẫn có thể (và nên) viết các hàm trong sạch bất cứ khi nào hợp lý.

Không có gì tệ hơn việc phải gỡ lỗi (debug) một chương trình mà ở đó thứ tự gọi hàm phải ***cực kỳ chính xác*** chỉ vì tất cả chúng đều đọc và sửa đổi cùng một biến toàn cục (global variable).