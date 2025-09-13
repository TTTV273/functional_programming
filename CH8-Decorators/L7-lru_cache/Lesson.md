# lru_cache

[`lru_cache` from the `functools` module](https://docs.python.org/3/library/functools.html#functools.lru_cache) is an example of a decorator and an example of memoization.

`lru_cache` memoizes the inputs and outputs of the decorated function in a size-restricted dictionary. It speeds up repeated calls to a slow function with the same inputs. For instance, if the function reads from disk, makes network requests, or requires a lot of computation AND it is used repeatedly with the same inputs.

Here's an example from the Python documentation that perfectly illustrates how and why to use the `lru_cache` decorator:

```python
from functools import lru_cache

@lru_cache()
def factorial_r(x):
    if x == 0:
        return 1
    else:
        return x * factorial_r(x - 1)

factorial_r(10) # no previously cached result, makes 11 recursive calls
# 3628800
factorial_r(5)  # just looks up cached value result
# 120
factorial_r(12) # makes two new recursive calls, the other 11 are cached
# 479001600
```

Since the `factorial` function is recursive and the inputs are sequential numbers, it's called repeatedly with the same inputs. Without the cache, the function would be called 30 times. With `lru_cache`, the function is only called 13 times. While you don't often need to compute factorials, this example ties together how to use a decorator _and_ memoization _and_ recursion.

## Assignment

The creator of Doc2Doc is a huge fan of [palindromes](https://en.wikipedia.org/wiki/Palindrome) for some nerdy reason. Add a feature to check if a word is a palindrome.

1. Import the `lru_cache` function from the `functools` module and use it to decorate the incomplete `is_palindrome` function.
2. Complete the `is_palindrome` function. It takes as input a `word` string and returns `True` if the word is a palindrome (such as "racecar"), or `False` otherwise.

Try to use recursion. Check the outer characters first, then move inwards until you reach the base case or find the word is not a palindrome.

## Gemini Translation

Tất nhiên rồi. Việc nắm rõ bài học trước khi bắt tay vào làm là rất quan trọng. Dưới đây là nội dung `Lesson.md` được dịch sang tiếng Việt.

-----

# lru_cache

[`lru_cache` từ module `functools`](https://docs.python.org/3/library/functools.html#functools.lru_cache) là một ví dụ về decorator và cũng là một ví dụ về **ghi nhớ (memoization)**.

`lru_cache` ghi nhớ các đầu vào và đầu ra của hàm được "trang trí" (decorated function) vào một từ điển có kích thước giới hạn. Nó giúp **tăng tốc** các lệnh gọi lặp đi lặp lại đến một hàm xử lý chậm với cùng một đầu vào. Ví dụ, nếu hàm đó phải đọc dữ liệu từ đĩa, thực hiện yêu cầu mạng, hoặc đòi hỏi tính toán nhiều VÀ nó được sử dụng lặp đi lặp lại với cùng các tham số đầu vào.

Đây là một ví dụ từ tài liệu của Python minh họa hoàn hảo cách thức và lý do sử dụng decorator `lru_cache`:

```python
from functools import lru_cache

@lru_cache()
def factorial_r(x):
    if x == 0:
        return 1
    else:
        return x * factorial_r(x - 1)

factorial_r(10) # chưa có kết quả nào được cache, thực hiện 11 lần gọi đệ quy
# 3628800
factorial_r(5)  # chỉ cần tra cứu giá trị đã được cache
# 120
factorial_r(12) # thực hiện 2 lần gọi đệ quy mới, 11 lần gọi kia đã được cache
# 479001600
```

Vì hàm `factorial` là đệ quy và các đầu vào là các số tuần tự, nó được gọi lặp đi lặp lại với cùng một đầu vào. Nếu không có cache, hàm sẽ được gọi **30 lần**. Với `lru_cache`, hàm chỉ được gọi **13 lần**. Mặc dù bạn không thường xuyên cần tính giai thừa, ví dụ này kết hợp cả cách sử dụng **decorator**, **memoization**, và **đệ quy**.

## Nhiệm vụ

Người tạo ra Doc2Doc là một fan hâm mộ lớn của [palindrome (từ đối xứng)](https://en.wikipedia.org/wiki/Palindrome) vì một lý do "mọt sách" nào đó. Hãy thêm một tính năng để kiểm tra xem một từ có phải là palindrome hay không.

1. Import hàm `lru_cache` từ module `functools` và sử dụng nó để "trang trí" cho hàm `is_palindrome` chưa hoàn chỉnh.
2. Hoàn thành hàm `is_palindrome`. Hàm này nhận đầu vào là một chuỗi `word` và trả về `True` nếu từ đó là một palindrome (ví dụ như "racecar"), hoặc `False` trong trường hợp ngược lại.

Hãy thử sử dụng **đệ quy**. Kiểm tra các ký tự bên ngoài trước, sau đó di chuyển vào trong cho đến khi bạn đạt đến trường hợp cơ sở (base case) hoặc thấy rằng từ đó không phải là palindrome.

-----

Bây giờ sau khi đã hiểu rõ hơn về `lru_cache` và đệ quy, chúng ta quay lại với bước đầu tiên nhé. Bạn sẽ import `lru_cache` và áp dụng nó như một decorator cho hàm `is_palindrome` như thế nào?

```python
# main.py

# ?


# ?
def is_palindrome(word):
    pass
```