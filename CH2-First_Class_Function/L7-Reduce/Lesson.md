# Reduce

The built-in [functools.reduce()](https://docs.python.org/3/library/functools.html#functools.reduce) function takes a function and a list of values, and applies the function to each value in the list, *accumulating a single result* as it goes.

![Reduce diagram](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/YU2hRLU-733x628.png)

```python
# import functools from the standard library
import functools

def add(sum_so_far, x):
    print(f"sum_so_far: {sum_so_far}, x: {x}")
    return sum_so_far + x

numbers = [1, 2, 3, 4]
sum = functools.reduce(add, numbers)
# sum_so_far: 1, x: 2
# sum_so_far: 3, x: 3
# sum_so_far: 6, x: 4
# 10 doesn't print, it's just the final result
print(sum)
# 10
```

Notice that we are passing the function `add` without the `()`.

It means that `reduce` will take care of the execution and pass the parameters for you.

Think of passing `add` like handing someone a recipe (the instructions), instead
of the finished dish (the result of the execution).

## Assignment

Complete the `join` and the `join_first_sentences` functions.

1. Complete the `join` function. It's a helper function we'll use in `join_first_sentences`.
   1. It takes two inputs:
      - A `doc_so_far` accumulator string - similar to the `sum_so_far` variable in the example above.
      - A `sentence` string - this is the next string we want to add to the accumulator.
   2. Returns the result of concatenating the "doc" and "sentence" strings together, with a period and a space in between. For example:

```python
doc = "This is the first sentence"
sentence = "This is the second sentence"
print(join(doc, sentence))
# This is the first sentence. This is the second sentence
```

2. Complete the `join_first_sentences` function.
   1. It accepts two arguments:
      - A list of sentence strings
      - An integer `n`
   2. Only use the first `n` sentences from the list. If `n` is zero, just return an empty string.
   3. Use [functools.reduce()](https://docs.python.org/3/library/functools.html#functools.reduce) with your `join` function to combine the sliced sentences into a single string.
   4. Add a final period without a trailing space and return this string.

**Tip:** Use [list slicing](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations) to get the first `n` sentences.

Here's an example of the expected behavior:

```python
joined = join_first_sentences(
    ["This is the first sentence", "This is the second sentence", "This is the third sentence"],
    2
)
print(joined)
# This is the first sentence. This is the second sentence.
```

## Gemini Translation

### Hàm `reduce` (Rút gọn/Tích tụ) ❄️

Hàm `reduce` là người bạn cuối cùng trong bộ ba. Nếu `map` là *biến đổi* và `filter` là *lựa chọn*, thì `reduce` là **tích tụ**. Nó sẽ lấy một danh sách và "gộp" tất cả các phần tử lại để cho ra **một kết quả duy nhất**.

Hãy tưởng tượng anh đang lăn một quả cầu tuyết. Anh bắt đầu với một nắm tuyết nhỏ, sau đó lăn nó qua lớp tuyết mới, quả cầu sẽ lớn dần lên. `reduce` hoạt động y hệt như vậy.

```python
# Cần phải import hàm reduce từ thư viện functools
import functools

# Hàm này cần 2 đầu vào:
# 1. Quả cầu tuyết từ bước trước (sum_so_far)
# 2. Lớp tuyết mới cần lăn qua (x)
def add(sum_so_far, x):
    print(f"sum_so_far: {sum_so_far}, x: {x}")
    return sum_so_far + x

numbers = [1, 2, 3, 4]
# reduce sẽ tự động lặp và "tích tụ" kết quả
sum = functools.reduce(add, numbers)
# Quá trình chạy:
# sum_so_far: 1, x: 2   -> kết quả là 3
# sum_so_far: 3, x: 3   -> kết quả là 6
# sum_so_far: 6, x: 4   -> kết quả là 10
print(sum)
# 10
```

Lưu ý rằng chúng ta truyền hàm `add` vào mà không có dấu `()`. Điều này giống như việc anh đưa cho `reduce` một "bản công thức" thay vì một "món ăn đã nấu xong". `reduce` sẽ tự dùng công thức đó để nấu.

### Bài tập

Hoàn thành 2 hàm: `join` và `join_first_sentences`.

**1. Hoàn thành hàm `join`:** Đây là hàm phụ trợ.

  * Nó nhận 2 đầu vào:
      * `doc_so_far`: Chuỗi đã được nối từ các bước trước (quả cầu tuyết).
      * `sentence`: Câu mới cần nối vào (lớp tuyết mới).
  * Trả về kết quả của việc nối `doc_so_far` và `sentence` lại với nhau, có một dấu chấm và một khoảng trắng ở giữa (`. `).

**Ví dụ:**

```python
doc = "Đây là câu đầu tiên"
sentence = "Đây là câu thứ hai"
print(join(doc, sentence))
# Kết quả: Đây là câu đầu tiên. Đây là câu thứ hai
```

**2. Hoàn thành hàm `join_first_sentences`:**

  * Nhận 2 đầu vào:
      * Một danh sách các câu.
      * Một số nguyên `n`.
  * Chỉ sử dụng `n` câu đầu tiên trong danh sách. Nếu `n` bằng 0, trả về một chuỗi rỗng.
  * Sử dụng `functools.reduce()` với hàm `join` của anh để kết hợp các câu đã cắt thành một chuỗi duy nhất.
  * Thêm một dấu chấm cuối cùng (không có khoảng trắng) và trả về chuỗi này.

**Mẹo:** Dùng kỹ thuật **cắt danh sách** (list slicing) để lấy `n` câu đầu tiên.

**Ví dụ kết quả mong muốn:**

```python
joined = join_first_sentences(
    ["Đây là câu đầu tiên", "Đây là câu thứ hai", "Đây là câu thứ ba"],
    2
)
print(joined)
# Kết quả: Đây là câu đầu tiên. Đây là câu thứ hai.
```