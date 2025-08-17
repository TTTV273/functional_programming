# Map

"Map", "filter", and "reduce" are three commonly used [higher-order functions](https://en.wikipedia.org/wiki/Higher-order_function) in functional programming.

In Python, the built-in [map](https://docs.python.org/3/library/functions.html#map) function takes a function and an [iterable](https://docs.python.org/3/glossary.html#term-iterable) (in this case a list) as inputs. It returns an iterator that applies the function to every item, yielding the results.

With `map`, we can operate on lists without using loops and nasty stateful variables. For example, given this code:

```python
def square(x):
    return x * x

nums = [1, 2, 3, 4, 5]
squared_nums = []
for num in nums:
    num_squared = square(num)
    squared_nums.append(num_squared)

print(squared_nums)
# [1, 4, 9, 16, 25]
```

We could use `map` instead, like this:

```python
def square(x):
    return x * x

nums = [1, 2, 3, 4, 5]
squared_nums = map(square, nums)

print(list(squared_nums))
# [1, 4, 9, 16, 25]
```

> **Note:** `map()` returns a "map object", so the [`list()` type constructor](https://docs.python.org/3/library/stdtypes.html#list) is needed to convert it back into a standard list.

## Assignment

[Markdown](https://www.markdownguide.org/cheat-sheet/) supports two different styles of bullet points, `-` and `*`. We prefer `*`, so, we need a function to convert any `-` bullet points to `*` bullet points.

Complete the `change_bullet_style` function. It takes a document (a string) as input, and returns a single string as output. The returned string should have any lines that start with a `-` character replaced with a `*` character.

For example, this:

```
- This is a bullet
- This is a bullet
```

Becomes:

```
* This is a bullet
* This is a bullet
```

Use the built-in [map](https://docs.python.org/3/library/functions.html#map) function to apply the provided `convert_line` function to each line of the input string. Use [.split()](https://docs.python.org/3/library/stdtypes.html#str.split) and [.join()](https://docs.python.org/3/library/stdtypes.html#str.join) to split the document into a list of lines, and then join the lines back together. This should preserve the original line breaks. Don't use the `.replace()` string method.

Examples of split and join:

```python
# my_document is a string with newlines
lines_list = my_document.split("\n")

rejoined_doc = "\n".join(lines_list)
```

## Gemini Translate

### Hàm `map` 🗺️

Trong lập trình hàm, có ba người bạn thân rất nổi tiếng là `map`, `filter`, và `reduce`. Chúng đều là **hàm bậc cao** (higher-order functions).

> **Hàm bậc cao là gì?** 🧠
>
> Cứ tưởng tượng nó như một cái máy đa năng. Thay vì chỉ xử lý dữ liệu (như số, chữ), nó có thể "nuốt" cả một hàm khác vào để làm việc, hoặc "nhả" ra một hàm mới tinh.

Trong Python, hàm `map` có sẵn hoạt động như một dây chuyền sản xuất tự động. Anh cần cung cấp cho nó hai thứ:

1. Một **hàm** (giống như một bản thiết kế, ví dụ: "bình phương hóa một số").
2. Một **dữ liệu lặp được** (iterable), ví dụ như một danh sách `list` (một thùng nguyên liệu thô).

`map` sẽ trả về một "đối tượng map" (gọi là iterator). Nó giống như một người quản đốc cầm bản thiết kế và đi qua từng món nguyên liệu, áp dụng bản thiết kế đó lên từng món một để tạo ra sản phẩm mới.

Nhờ `map`, chúng ta có thể xử lý cả một danh sách mà không cần dùng vòng lặp `for` và các biến tạm lỉnh kỉnh.

**Ví dụ, cách làm thông thường:**

```python
def square(x):
    return x * x

nums = [1, 2, 3, 4, 5]
squared_nums = []
for num in nums:
    num_squared = square(num)
    squared_nums.append(num_squared)

print(squared_nums)
# [1, 4, 9, 16, 25]
```

**Và đây là cách dùng `map` gọn gàng hơn:**

```python
def square(x):
    return x * x

nums = [1, 2, 3, 4, 5]
squared_nums = map(square, nums)

print(list(squared_nums))
# [1, 4, 9, 16, 25]
```

> **Lưu ý quan trọng:** `map()` chỉ trả về một "đối tượng map", giống như một lời hứa "tôi sẽ xử lý khi anh cần". Để xem kết quả thực sự, anh cần dùng hàm `list()` để chuyển nó thành một danh sách hoàn chỉnh.

### Bài tập

Trong Markdown, mình có thể dùng dấu `-` hoặc `*` để tạo danh sách. Giả sử team mình quy định chỉ dùng dấu `*`. Anh cần một hàm để tự động "chuẩn hóa" lại văn bản.

**Nhiệm vụ:** Hoàn thành hàm `change_bullet_style`.

* **Đầu vào**: Một văn bản (kiểu `string`).
* **Đầu ra**: Một văn bản duy nhất, trong đó những dòng bắt đầu bằng `-` đã được đổi thành `*`.

**Ví dụ:**

```
- Đây là một gạch đầu dòng
- Đây cũng vậy
```

**Sẽ biến thành:**

```
* Đây là một gạch đầu dòng
* Đây cũng vậy
```

**Yêu cầu:**

* Sử dụng hàm `map` để áp dụng hàm `convert_line` có sẵn cho mỗi dòng.
* Dùng `.split("\n")` để tách văn bản thành danh sách các dòng.
* Dùng `"\n".join()` để ghép các dòng lại thành một văn bản.
* Không được dùng hàm `.replace()`.