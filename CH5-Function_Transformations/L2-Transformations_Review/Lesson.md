# Transformations Review

Example of a function transformation:

```python
def multiply(x, y):
    return x * y

def add(x, y):
    return x + y

def self_math(math_func):
    # inner_func is defined inside self_math.
    # It can only be referenced directly
    # inside self_math's scope. However, it is then
    # returned and can be captured into a new variable
    # like square_func or double_func, and called that way
    def inner_func(x):
        return math_func(x, x)
    return inner_func

square_func = self_math(multiply)
double_func = self_math(add)

print(square_func(5))
# 25

print(double_func(5))
# 10
```

## Gemini Translation

# Ôn tập về Biến Đổi Hàm

Ví dụ về một biến đổi hàm:

```python
def multiply(x, y):
    return x * y

def add(x, y):
    return x + y

def self_math(math_func):
    # inner_func được định nghĩa bên trong self_math.
    # Nó chỉ có thể được tham chiếu trực tiếp
    # bên trong phạm vi của self_math. Tuy nhiên, sau đó nó được
    # trả về và có thể được gán vào một biến mới
    # như square_func hoặc double_func, và được gọi theo cách đó
    def inner_func(x):
        return math_func(x, x)
    return inner_func

square_func = self_math(multiply)
double_func = self_math(add)

print(square_func(5))
# 25

print(double_func(5))
# 10
```