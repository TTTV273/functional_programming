# First Class and Higher Order Functions

A programming language "supports first-class functions" when functions are treated like any other variable. That means functions can be passed as arguments to other functions, can be returned by other functions, and can be assigned to variables.

- **First-class function:** A function that is treated like any other value
- **Higher-order function:** A function that accepts another function as an argument or returns a function

Python supports first-class and higher-order functions.

## First-Class Example

```python
def square(x):
    return x * x

# Assign function to a variable
f = square

print(f(5))
# 25
```

## Higher-Order Example

```python
def square(x):
    return x * x

def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result

squares = my_map(square, [1, 2, 3, 4, 5])
print(squares)
# [1, 4, 9, 16, 25]
```

## Gemini Translate

### Hàm Hạng Nhất và Hàm Bậc Cao

Một ngôn ngữ lập trình được gọi là "hỗ trợ hàm hạng nhất" khi các hàm trong nó được đối xử giống như mọi biến thông thường khác. Điều này có nghĩa là hàm có thể được **truyền vào làm tham số** cho một hàm khác, có thể được **trả về từ một hàm khác**, và có thể được **gán cho một biến**.

- **Hàm hạng nhất (First-class function):** Một hàm được đối xử như mọi giá trị khác. Tưởng tượng nó giống như một con số hay một chuỗi văn bản, bạn có thể "cầm" nó, "cất" vào một cái hộp (biến), hoặc "đưa" nó cho người khác (hàm khác).

- **Hàm bậc cao (Higher-order function):** Đây là một hàm "làm việc với các hàm khác". Cụ thể, nó là một hàm nhận một hàm khác làm tham số đầu vào, hoặc kết quả trả về của nó là một hàm.

Python hỗ trợ cả hai khái niệm này.

### Ví dụ về Hàm Hạng Nhất

Trong ví dụ này, chúng ta xem cách một hàm có thể được đối xử như một biến thông thường.

```python
# Định nghĩa một hàm bình thường tên là square
def square(x):
    return x * x

# Gán chính hàm đó cho một biến mới tên là f
# Lưu ý: ta không gọi hàm square(), mà ta đang gán chính "bản thể" của hàm
f = square

# Bây giờ, biến f chính là hàm square, ta có thể gọi nó
print(f(5))
# Kết quả: 25
```

### Ví dụ về Hàm Bậc Cao

Ở đây, `my_map` chính là một hàm bậc cao vì nó nhận một hàm khác (`func`) làm tham số đầu vào.

```python
# Một hàm bình thường để tính bình phương
def square(x):
    return x * x

# Một hàm bậc cao tên là my_map
# Nó nhận vào một hàm (func) và một danh sách (arg_list)
def my_map(func, arg_list):
    result = []
    # Lặp qua từng phần tử trong danh sách
    for i in arg_list:
        # Gọi hàm "func" với từng phần tử và thêm kết quả vào danh sách mới
        result.append(func(i))
    return result

# Gọi hàm my_map, truyền hàm "square" vào làm tham số đầu tiên
squares = my_map(square, [1, 2, 3, 4, 5])

print(squares)
# Kết quả: [1, 4, 9, 16, 25]
```
