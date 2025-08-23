# Reference vs. Value

When you pass a value into a function as an argument, one of two things can happen:

- It's passed by **reference**: The function has access to the original value and can change it.
- It's passed by **value**: The function only has access to a copy. Changes to the copy within the function don't affect the original.

*There is a bit more nuance, but this explanation mostly works.*

These types are passed by **reference**:

- Lists
- Dictionaries
- Sets

These types are passed by **value**:

- Integers
- Floats
- Strings
- Booleans
- Tuples

Most collection types are passed by reference (except for tuples) and most primitive types are passed by value.

## Example of Pass by Reference (Mutable)

```python
def modify_list(inner_lst):
    inner_lst.append(4)
    # the original "outer_lst" is updated
    # because inner_lst is a reference to the original

outer_lst = [1, 2, 3]
modify_list(outer_lst)
# outer_lst = [1, 2, 3, 4]
```

## Example of Pass by Value (Immutable)

```python
def attempt_to_modify(inner_num):
    inner_num += 1
    # the original "outer_num" is not updated
    # because inner_num is a copy of the original

outer_num = 1
attempt_to_modify(outer_num)
# outer_num = 1
```

## Assignment

We have a way for Doc2Doc users to set their supported formats in their settings. In memory, we store those settings as a simple dictionary:

```python
settings = {
    "docx": True,
    "pdf": True,
    "txt": False
}
```

Unfortunately, there is a bug in our code! When a new format is added or removed, it not only updates the new dictionary, but it changes the defaults themselves! That's not good. We want to create a *new* dictionary with the updates, not change the original.

Fix the bug by making `add_format` and `remove_format` pure functions that don't mutate their inputs.

## Tip

Simply assigning a new variable to an existing dictionary doesn't copy that dictionary, it points to the same dictionary. Instead, use the [.copy()](https://docs.python.org/3/library/stdtypes.html#dict.copy) method to create a new copy of a dictionary.

## Gemini Translation

### **# Truyền Tham Chiếu (Reference) và Truyền Tham Trị (Value)**

Khi bạn truyền một giá trị vào một hàm dưới dạng đối số, một trong hai điều sau sẽ xảy ra:

* **Truyền bằng tham chiếu (pass by reference):** Hàm có quyền truy cập vào **giá trị gốc** và có thể thay đổi nó.
* **Truyền bằng tham trị (pass by value):** Hàm chỉ có quyền truy cập vào một **bản sao (copy)**. Những thay đổi trên bản sao bên trong hàm sẽ không ảnh hưởng đến giá trị gốc.

*(Thực tế có một chút khác biệt tinh tế hơn, nhưng cách giải thích này về cơ bản là đúng.)*

-----

Các kiểu dữ liệu sau được truyền bằng **tham chiếu**:

* `List` (danh sách)
* `Dictionary` (từ điển)
* `Set` (tập hợp)

Các kiểu dữ liệu sau được truyền bằng **tham trị**:

* `Integer` (số nguyên)
* `Float` (số thực)
* `String` (chuỗi)
* `Boolean` (logic đúng/sai)
* `Tuple`

Hầu hết các kiểu dữ liệu dạng bộ sưu tập (collection) được truyền bằng tham chiếu (trừ `tuple`), và hầu hết các kiểu dữ liệu nguyên thủy (primitive) được truyền bằng tham trị.

-----

#### **Ví dụ về Truyền bằng Tham chiếu (Mutable - Có thể thay đổi)**

```python
def modify_list(inner_lst):
    inner_lst.append(4)
    # danh sách "outer_lst" ban đầu bị cập nhật
    # bởi vì inner_lst là một tham chiếu đến bản gốc

outer_lst = [1, 2, 3]
modify_list(outer_lst)
# bây giờ outer_lst là [1, 2, 3, 4]
```

#### **Ví dụ về Truyền bằng Tham trị (Immutable - Bất biến)**

```python
def attempt_to_modify(inner_num):
    inner_num += 1
    # số "outer_num" ban đầu không bị cập nhật
    # bởi vì inner_num là một bản sao của bản gốc

outer_num = 1
attempt_to_modify(outer_num)
# outer_num vẫn là 1
```

-----

### **## Bài Tập**

Chúng ta có một cách để người dùng Doc2Doc thiết lập các định dạng được hỗ trợ trong phần cài đặt của họ. Trong bộ nhớ, chúng ta lưu các cài đặt đó dưới dạng một dictionary đơn giản:

```python
settings = {
    "docx": True,
    "pdf": True,
    "txt": False
}
```

Không may là có một lỗi trong code của chúng ta! Khi một định dạng mới được thêm vào hoặc xóa đi, nó không chỉ cập nhật dictionary mới mà còn **thay đổi cả các cài đặt mặc định gốc!** Điều này không tốt. Chúng ta muốn tạo ra một dictionary *mới* với các cập nhật, chứ không phải thay đổi bản gốc.

**Nhiệm vụ:** Hãy sửa lỗi bằng cách biến `add_format` và `remove_format` thành các hàm thuần khiết không làm thay đổi (mutate) đầu vào của chúng.

-----

### **## Gợi ý (Tip)**

Việc gán một biến mới cho một dictionary đã có không tạo ra bản sao của dictionary đó, mà nó chỉ trỏ đến cùng một dictionary. Thay vào đó, hãy sử dụng phương thức `[.copy()](https://docs.python.org/3/library/stdtypes.html#dict.copy)` để tạo một bản sao mới của một dictionary.

-----

Để dễ hình dung, anh hãy nghĩ về nó như thế này:

* **Truyền bằng tham trị** giống như đưa cho ai đó một **bản photocopy** 📄. Họ có thể viết vẽ lên bản photocopy đó thoải mái, nhưng bản gốc của anh vẫn sạch sẽ.
* **Truyền bằng tham chiếu** giống như gửi cho ai đó một **đường link Google Docs** 🔗. Bất kỳ ai có link đều đang chỉnh sửa trên cùng một tài liệu gốc.

Dựa vào sự khác biệt đó, anh có thể giải thích tại sao hàm `modify_list` ở ví dụ trên lại làm thay đổi `outer_lst`, còn hàm `attempt_to_modify` thì không làm thay đổi `outer_num` không?