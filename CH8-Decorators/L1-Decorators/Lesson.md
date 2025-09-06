# Decorators

Remember function transformations where a (higher-order) function takes a function and returns a function with new behavior? [Python decorators](https://docs.python.org/3/glossary.html#term-decorator) are just [syntactic sugar](https://en.wikipedia.org/wiki/Syntactic_sugar) around that.

**Example:**

```python
def vowel_counter(func_to_decorate):
    vowel_count = 0
    def wrapper(doc):
        nonlocal vowel_count
        vowels = "aeiou"
        for char in doc:
            if char in vowels:
                vowel_count += 1
        print(f"Vowel count: {vowel_count}")
        return func_to_decorate(doc)
    return wrapper

@vowel_counter
def process_doc(doc):
    print(f"Document: {doc}")

process_doc("What")
# Vowel count: 1
# Document: What

process_doc("a wonderful")
# Vowel count: 5
# Document: a wonderful

process_doc("world")
# Vowel count: 6
# Document: world
```

The `@vowel_counter` line is "decorating" the `process_doc` function with the `vowel_counter` function. `vowel_counter` is called once when `process_doc` is defined with the `@` syntax, but the `wrapper` function that it returns is called every time `process_doc` is called. That's why `vowel_count` is preserved and printed after each time.

## It's Just Syntactic Sugar

Python decorators are just another (sometimes simpler) way of writing a higher-order function. These two pieces of code are *identical*:

### With Decorator

```python
@vowel_counter
def process_doc(doc):
    print(f"Document: {doc}")

process_doc("Something wicked this way comes")
```

### Without Decorator

```python
def process_doc(doc):
    print(f"Document: {doc}")

process_doc = vowel_counter(process_doc)
process_doc("Something wicked this way comes")
```

## Assignment

The provided `file_type_aggregator` function is intended to decorate other functions. It assumes that the function it decorates has exactly 2 positional arguments.

**Create a `process_doc` function** that's decorated by `file_type_aggregator`. It should return the following string:

```python
f"Processing doc: '{doc}'. File Type: {file_type}"
```

Where `doc` and `file_type` are its positional arguments. (See line 11 for where it's being called)

## Gemini Translation

### Decorator

Bạn có nhớ các phép biến đổi hàm (function transformation) không? Đó là nơi một hàm (bậc cao hơn) nhận vào một hàm và trả về một hàm khác với hành vi mới. [Decorator trong Python](https://docs.python.org/3/glossary.html#term-decorator) thực chất chỉ là một cách viết khác, hay còn gọi là [syntactic sugar](https://en.wikipedia.org/wiki/Syntactic_sugar), cho khái niệm đó.

**Ví dụ:**

```python
def vowel_counter(func_to_decorate):
    vowel_count = 0
    def wrapper(doc):
        nonlocal vowel_count
        vowels = "aeiou"
        for char in doc:
            if char in vowels:
                vowel_count += 1
        print(f"Số nguyên âm: {vowel_count}")
        return func_to_decorate(doc)
    return wrapper

@vowel_counter
def process_doc(doc):
    print(f"Tài liệu: {doc}")

process_doc("What")
# Số nguyên âm: 1
# Tài liệu: What

process_doc("a wonderful")
# Số nguyên âm: 5
# Tài liệu: a wonderful

process_doc("world")
# Số nguyên âm: 6
# Tài liệu: world
```

Dòng `@vowel_counter` đang "trang trí" (decorating) hàm `process_doc` bằng hàm `vowel_counter`. Hàm `vowel_counter` được gọi một lần khi hàm `process_doc` được định nghĩa bằng cú pháp `@`, nhưng hàm `wrapper` mà nó trả về sẽ được gọi mỗi khi `process_doc` được gọi. Đó là lý do tại sao `vowel_count` được lưu giữ và in ra sau mỗi lần gọi.

#### Nó chỉ là "Syntactic Sugar"

Decorator trong Python chỉ là một cách khác (đôi khi đơn giản hơn) để viết một hàm bậc cao. Hai đoạn mã dưới đây là *giống hệt nhau*:

##### Với Decorator

```python
@vowel_counter
def process_doc(doc):
    print(f"Tài liệu: {doc}")

process_doc("Something wicked this way comes")
```

### Không có Decorator

```python
def process_doc(doc):
    print(f"Tài liệu: {doc}")

process_doc = vowel_counter(process_doc)
process_doc("Something wicked this way comes")
```

#### Bài tập 📝

Hàm `file_type_aggregator` được cung cấp nhằm mục đích trang trí cho các hàm khác. Nó giả định rằng hàm mà nó trang trí có chính xác 2 đối số vị trí (positional arguments).

**Tạo một hàm `process_doc`** được trang trí bởi `file_type_aggregator`. Hàm này nên trả về chuỗi sau:

```python
f"Đang xử lý tài liệu: '{doc}'. Loại tệp: {file_type}"
```

Trong đó `doc` và `file_type` là các đối số vị trí của nó. (Xem dòng 11 để biết nơi nó đang được gọi)
