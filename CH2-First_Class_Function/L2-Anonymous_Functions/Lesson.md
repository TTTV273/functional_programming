# Anonymous Functions

Anonymous functions have *no name*, and in Python, they're called [lambda functions](https://docs.python.org/3/reference/expressions.html#lambda) after [lambda calculus](https://en.wikipedia.org/wiki/Lambda_calculus). Here's a lambda function that takes a single argument `x` and returns the result of `x + 1`:

```python
lambda x: x + 1
```

Notice that the [expression](https://docs.python.org/3/reference/expressions.html#expressions) `x + 1` is returned *automatically*, no need for a `return` statement. And because functions are just values, we can assign the function to a variable named `add_one`:

```python
add_one = lambda x: x + 1
print(add_one(2))
# 3
```

Lambda functions might *look* scary, but they're still just functions. Because they simply return the result of an expression, they're often used for small, simple evaluations. Here's an example that uses a lambda to get a value from a dictionary:

```python
get_age = lambda name: {
    "lane": 29,
    "hunter": 69,
    "allan": 17
}.get(name, "not found")
print(get_age("lane"))
# 29
```

## Assignment

Complete the `file_type_getter` function. This function accepts a list of tuples, where each tuple contains:

1. A "file type" (e.g. "code", "document", "image", etc)
2. A list of associated file extensions (e.g. `[".py", ".js"]` or `[".docx", ".doc"]`)

The function returns a function for looking up the file type of a given file extension.

1. Create an empty dictionary to map each file extension to its file type.
2. Loop through the `file_extension_tuples`:
   1. Loop through the file extensions.
   2. Add each extension to the dictionary and assign its value to the file type.

For example, if given the following list of tuples:

```python
# list of tuples
[
    ("document", [".doc", ".docx"]),
    ("image", [".jpg", ".png"])
]

# resulting dictionary
{
    ".doc": "document",
    ".docx": "document",
    ".jpg": "image",
    ".png": "image",
}
```

3. Return a lambda function that accepts a string (a file extension) and returns its file type from the dictionary.
4. Use the [.get](https://docs.python.org/3/library/stdtypes.html#dict.get) dictionary method in the lambda function to return the file type of the extension if found or `"Unknown"` if it's missing.

## Gemini

Dưới đây là tóm tắt những điểm chính chúng ta đã thảo luận để làm rõ hơn về bài học này.

### 1. Vòng Lặp "Mở Gói" (Unpacking)

Một điểm gây khó hiểu ban đầu là cú pháp `for file_type, extensions in file_extension_tuples:`. Đây là một tính năng mạnh mẽ của Python gọi là "unpacking".

- **Tưởng tượng**: `file_extension_tuples` là một danh sách các chiếc hộp, mỗi hộp chứa một cặp gồm 2 món.
- **Cách hoạt động**: Thay vì lấy ra cả chiếc hộp, vòng lặp `for` sẽ tự động "mở gói" và gán món đầu tiên cho biến `file_type`, món thứ hai cho biến `extensions`.

Điều này giúp code gọn gàng hơn rất nhiều so với việc dùng một biến rồi truy cập qua chỉ số (`item[0]`, `item[1]`).

### 2. Lambda và "Closure": Robot và Chiếc Ba Lô

Khái niệm trừu tượng nhất là tại sao hàm `lambda` trả về lại có thể sử dụng được biến `extension_map`.

- **Nhà máy và Robot**: Hãy coi hàm `file_type_getter` như một "nhà máy". Nhiệm vụ của nó không phải để tra cứu, mà là để "sản xuất" ra một con robot chuyên tra cứu.
- **Bộ não & Ba lô**: Khi nhà máy hoạt động, nó xây dựng nên một "bộ não" (`extension_map`). Sau đó, nó tạo ra một con robot (`lambda`) và "đóng gói" bộ não đó vào trong một chiếc ba lô mà con robot luôn mang theo.
- **Closure**: Việc con robot `lambda` "nhớ" được bộ não `extension_map` từ nơi nó được sinh ra được gọi là **closure**.

Khi bạn gọi `file_checker('.jpg')`, bạn đang ra lệnh cho con robot, và nó sẽ dùng chính bộ não trong ba lô của mình để tra cứu và trả lời.

### 3. Cải tiến Code: Tách biệt Nhiệm vụ

Chúng ta nhận ra rằng việc "nhà máy" phải xây lại "bộ não" mỗi lần sản xuất robot là không hiệu quả. Vì vậy, chúng ta đã cải tiến code bằng cách tách biệt 2 nhiệm vụ:

**Cách cũ: Gộp 2 việc**
```python
def file_type_getter(file_extension_tuples):
    # Việc 1: Xây dựng "bộ não"
    extension_map = {}
    for file_type, extensions in file_extension_tuples:
        for extension in extensions:
            extension_map[extension] = file_type
            
    # Việc 2: Sản xuất "robot"
    return lambda extension: extension_map.get(extension, "Unknown")
```

**Cách mới: Tách riêng 2 việc**
```python
# Việc 1: Hàm chuyên xây dựng "bộ não" (chỉ chạy 1 lần)
def build_extension_map(file_extension_tuples):
    extension_map = {}
    for file_type, extensions in file_extension_tuples:
        for extension in extensions:
            extension_map[extension] = file_type
    return extension_map

# Việc 2: Hàm chuyên sản xuất "robot" từ "bộ não" có sẵn
def create_file_checker(extension_map):
    return lambda extension: extension_map.get(extension, "Unknown")
```
Cách tiếp cận mới này hiệu quả và rõ ràng hơn nhiều.