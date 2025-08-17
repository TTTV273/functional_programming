# Filter

The built-in [filter](https://docs.python.org/3/library/functions.html#filter) function takes a function and an iterable (in this case a list) and returns an iterator that only contains elements from the original iterable where the result of the function on that item returned `True`.

![Filter diagram](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/FfVxD7d-933x350.png)

In Python:

```python
def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(is_even, numbers))
print(evens)
# [2, 4, 6]
```

## Assignment

Complete the `remove_invalid_lines` function. It accepts a document as input. It should:

1. Use the built-in `filter` function and a lambda to return a filtered copy of the input document
2. *Remove* any lines that start with a `-` character.
3. Keep *all* other lines and **preserve trailing newlines**.

For example, this:

```
* Star Wars episode 1 is underrated
- Star Wars episode 9 is fine
* Star Wars episode 3 is the best

```

Should become:

```
* Star Wars episode 1 is underrated
* Star Wars episode 3 is the best

```

## Tips

The `splitlines` method does not preserve trailing newlines and may cause your output to fail the tests.

The following methods may be useful:

[.join](https://docs.python.org/3/library/stdtypes.html#str.join)

```python
"\n".join(["a", "b", "c"])
# a
# b
# c
```

[.startswith](https://docs.python.org/3/library/stdtypes.html#str.startswith)

```python
s = "hello"
s.startswith("h")
# True
s.startswith("o")
# False
```

[.split](https://docs.python.org/3/library/stdtypes.html#str.split)

```python
s = """hello
world"""
lines = s.split("\n")
# ['hello', 'world']
```

## Gemini Translation

### Hàm `filter` (Bộ lọc) 🚦

`filter` là người bạn thứ hai trong bộ ba `map`, `filter`, `reduce`. Nếu `map` là một dây chuyền sản xuất *biến đổi* mọi thứ đi qua nó, thì `filter` là một **nhân viên kiểm tra chất lượng**.

Nhiệm vụ của `filter` là nhận vào một hàm (một "bộ quy tắc") và một danh sách, sau đó nó sẽ trả về một danh sách mới chỉ chứa những phần tử **vượt qua** được bộ quy tắc đó.

Hàm mà anh đưa cho `filter` phải là một hàm trả về `True` (Đúng) hoặc `False` (Sai).

  * Nếu hàm trả về `True` -> "Đạt chuẩn! Cho qua."
  * Nếu hàm trả về `False` -> "Không đạt! Loại."

**Trong Python:**

```python
# Hàm này là "bộ quy tắc", nó hỏi: "x có phải là số chẵn không?"
def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
# filter sẽ dùng is_even để kiểm tra từng số trong numbers
evens = list(filter(is_even, numbers))
print(evens)
# Kết quả chỉ chứa những số "đạt chuẩn" (là số chẵn)
# [2, 4, 6]
```

### Bài tập

Hoàn thành hàm `remove_invalid_lines`. Hàm này nhận đầu vào là một văn bản. Nó cần phải:

1.  Dùng hàm `filter` và một **hàm lambda** (hàm ẩn danh) để trả về một bản sao đã được lọc của văn bản.
2.  **Loại bỏ** bất kỳ dòng nào bắt đầu bằng ký tự `-`.
3.  **Giữ lại** tất cả các dòng khác và **bảo toàn các dấu xuống dòng ở cuối file**.

**Ví dụ, văn bản này:**

```
* Star Wars episode 1 is underrated
- Star Wars episode 9 is fine
* Star Wars episode 3 is the best

```

**Sẽ trở thành:**

```
* Star Wars episode 1 is underrated
* Star Wars episode 3 is the best

```

### Mẹo

  * Hàm `.splitlines()` sẽ không giữ lại dấu xuống dòng ở cuối, có thể làm bài test của anh bị lỗi.
  * Các hàm sau có thể hữu ích:
      * `.join`: Ghép một danh sách các chuỗi lại với nhau.
      * `.startswith("...")`: Kiểm tra xem một chuỗi có bắt đầu bằng một chuỗi con nào đó không (trả về `True`/`False`).
      * `.split("\n")`: Tách một chuỗi thành danh sách các dòng.