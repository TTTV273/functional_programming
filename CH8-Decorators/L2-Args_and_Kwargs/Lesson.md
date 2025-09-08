# Args and Kwargs

In Python, [`*args` and `**kwargs`](https://book.pythontips.com/en/latest/args_and_kwargs.html) allow a function to accept and deal with a *variable* number of arguments.

- `*args` collects positional arguments into a *tuple*
- `**kwargs` collects keyword (named) arguments into a *dictionary*

```python
def print_arguments(*args, **kwargs):
    print(f"Positional arguments: {args}")
    print(f"Keyword arguments: {kwargs}")

print_arguments("hello", "world", a=1, b=2)
# Positional arguments: ('hello', 'world')
# Keyword arguments: {'a': 1, 'b': 2}
```

## Positional Arguments

Positional arguments are the ones you're already familiar with, where the order of the arguments matters. Like this:

```python
def sub(a, b):
    return a - b

# a=3, b=2
res = sub(3, 2)
# res = 1
```

## Keyword Arguments

[Keyword arguments](https://docs.python.org/3/tutorial/controlflow.html#keyword-arguments) are passed in by name. *Order does not matter*. Like this:

```python
def sub(a, b):
    return a - b

res = sub(b=3, a=2)
# res = -1
res = sub(a=3, b=2)
# res = 1
```

## A Note on Ordering

Any positional arguments *must come before* keyword arguments. This will *not* work:

```python
sub(b=3, 2)
```

## Assignment

At Doc2Doc, we need better internal debugging tools. **Complete the `args_logger` function.** It takes a variable number of positional and keyword arguments and prints them to the console.

1. Print each positional argument *sequentially* using numbers and periods as the prefixes, starting with `1. `. For example:

```python
args_logger("what's", "up", "doc")
```

prints to the console:

```
1. what's
2. up
3. doc
```

2. Print each keyword argument *alphabetically by key* using asterisks (`*`) as the prefix with a colon (`:`) in between. For example:

```python
args_logger("hi", "there", age=17, date="July 4 1776")
```

prints to the console:

```
1. hi
2. there
* age: 17
* date: July 4 1776
```

*Use the [`sorted()`](https://docs.python.org/3/library/functions.html#sorted) function to get the order right.*

## Tips

- Don't feel guilty about using loops.
- `kwargs` is a dictionary, not a list. My recommendation is to use the [`.items()`](https://docs.python.org/3/library/stdtypes.html#dict.items) method to get its key-value pairs as a list of tuples, then sort that list before printing.

## Gemini Translation

### Args và Kwargs

Trong Python, [`*args` và `**kwargs`](https://book.pythontips.com/en/latest/args_and_kwargs.html) cho phép một hàm chấp nhận và xử lý một số lượng tham số *thay đổi*.

- `*args` thu thập các tham số vị trí (positional arguments) vào một `tuple`.
- `**kwargs` thu thập các tham số từ khóa (keyword/named arguments) vào một `dictionary`.

```python
def print_arguments(*args, **kwargs):
    print(f"Tham số vị trí: {args}")
    print(f"Tham số từ khóa: {kwargs}")

print_arguments("hello", "world", a=1, b=2)
# Tham số vị trí: ('hello', 'world')
# Tham số từ khóa: {'a': 1, 'b': 2}
```

#### Tham số vị trí (Positional Arguments)

Đây là loại tham số mà anh đã quen thuộc, trong đó thứ tự của các tham số là quan trọng. Giống như thế này:

```python
def sub(a, b):
    return a - b

# a=3, b=2
res = sub(3, 2)
# res = 1
```

#### Tham số từ khóa (Keyword Arguments)

[Tham số từ khóa](https://docs.python.org/3/tutorial/controlflow.html#keyword-arguments) được truyền vào bằng tên. *Thứ tự không quan trọng*. Giống như thế này:

```python
def sub(a, b):
    return a - b

res = sub(b=3, a=2)
# res = -1
res = sub(a=3, b=2)
# res = 1
```

#### Một lưu ý về thứ tự

Bất kỳ tham số vị trí nào cũng *phải đứng trước* tham số từ khóa. Đoạn code này sẽ *không* hoạt động:

```python
sub(b=3, 2)
```

#### Bài tập 📝

Tại Doc2Doc, chúng tôi cần các công cụ gỡ lỗi nội bộ tốt hơn. **Hãy hoàn thành hàm `args_logger`.** Hàm này nhận một số lượng thay đổi các tham số vị trí và từ khóa rồi in chúng ra console.

1. In mỗi tham số vị trí *tuần tự* bằng cách sử dụng số và dấu chấm làm tiền tố, bắt đầu bằng `1. `. Ví dụ:

```python
args_logger("what's", "up", "doc")
```

sẽ in ra console:

```
1. what's
2. up
3. doc
```

2. In mỗi tham số từ khóa *theo thứ tự alphabet của khóa (key)* bằng cách sử dụng dấu hoa thị (`*`) làm tiền tố với dấu hai chấm (`:`) ở giữa. Ví dụ:

```python
args_logger("hi", "there", age=17, date="July 4 1776")
```

sẽ in ra console:

```
1. hi
2. there
* age: 17
* date: July 4 1776
```

*Sử dụng hàm [`sorted()`](https://docs.python.org/3/library/functions.html#sorted) để có thứ tự đúng.*

#### Mẹo

- Đừng ngại sử dụng vòng lặp.
- `kwargs` là một dictionary, không phải là list. Tôi khuyên bạn nên sử dụng phương thức [`.items()`](https://docs.python.org/3/library/stdtypes.html#dict.items) để lấy các cặp khóa-giá trị của nó dưới dạng một danh sách các tuple, sau đó sắp xếp danh sách đó trước khi in.
