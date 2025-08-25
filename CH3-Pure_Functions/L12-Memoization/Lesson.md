# Memoization

At its core, [memoization](https://en.wikipedia.org/wiki/Memoization) is just [caching](https://en.wikipedia.org/wiki/Cache_(computing)) (storing a copy of) the result of a computation so that we don't have to compute it again in the future.

For example, take this simple function:

```python
def add(x, y):
    return x + y
```

A call to `add(5, 7)` will *always* evaluate to `12`. So, if you think about it, once we know that `add(5, 7)` can be replaced with `12`, we can just store the value `12` somewhere in memory so that we don't have to do the addition operation again in the future. Then, if we need to `add(5, 7)` again, we can just look up the value `12` instead of doing a (potentially expensive) CPU operation.

The slower and more complex the function, the more memoization can help speed things up.

> **Note:** It's pronounced "memOization", not "memORization". This confused me for quite a while in college, I thought my professor just didn't speak goodly...

## Assignment

Counting the words in a document can be slow, so we want to *memoize* it.

Complete the `word_count_memo` function. It takes two inputs:

1. A `document` string.
2. A `memos` dictionary. The keys are full document strings, and the values are the word count of the document.

It should return two values:

1. The word count of the given document
2. An updated `memos` dictionary.

Here are the steps to follow:

1. Create a [.copy()](https://docs.python.org/3/library/copy.html#module-copy) of the `memos` dictionary.
2. If the document is [in](https://docs.python.org/3/library/stdtypes.html#dict) the `memos` dictionary, just `return` the associated word count and the `memos` copy. No need to recompute the word count.
3. Otherwise, use the provided `word_count` function to count the words in the given `document`.
4. Store the word count in the `memos` copy.
5. `return` the word count and the updated `memos` copy.

## Gemini Translation (Bản Dịch Gemini)

### **# Memoization (Ghi nhớ hóa)**

Về cốt lõi, [memoization](https://en.wikipedia.org/wiki/Memoization) chỉ đơn giản là [caching](https://en.wikipedia.org/wiki/Cache_\(computing\)) (lưu trữ một bản sao) kết quả của một phép tính để chúng ta không phải tính toán lại nó trong tương lai.

Ví dụ, hãy xem hàm đơn giản này:

```python
def add(x, y):
    return x + y
```

Một lời gọi đến `add(5, 7)` sẽ *luôn luôn* trả về kết quả là `12`. Vì vậy, nếu bạn nghĩ về nó, một khi chúng ta biết `add(5, 7)` có thể được thay thế bằng `12`, chúng ta có thể chỉ cần lưu giá trị `12` ở đâu đó trong bộ nhớ để không phải thực hiện lại phép cộng trong tương lai. Sau đó, nếu chúng ta cần gọi lại `add(5, 7)`, chúng ta chỉ cần tra cứu giá trị `12` thay vì thực hiện một phép tính CPU (có thể tốn kém).

Hàm càng chậm và càng phức tạp, memoization càng giúp tăng tốc độ.

> **Lưu ý:** Nó được phát âm là "mem**O**ization", không phải "mem**OR**ization". Điều này đã làm tôi bối rối một thời gian khá dài ở đại học, tôi đã nghĩ rằng giáo sư của mình phát âm không chuẩn...

### **## Bài tập**

Việc đếm từ trong một tài liệu có thể chậm, vì vậy chúng ta muốn *ghi nhớ hóa* (memoize) nó.

Hoàn thành hàm `word_count_memo`. Nó nhận vào hai đầu vào:

1. Một chuỗi `document`.
2. Một từ điển `memos`. Các khóa (keys) là chuỗi tài liệu đầy đủ, và các giá trị (values) là số lượng từ của tài liệu đó.

Nó phải trả về hai giá trị:

1. Số lượng từ của tài liệu đã cho
2. Một từ điển `memos` đã được cập nhật.

Đây là các bước cần thực hiện:

1. Tạo một bản sao [.copy()](https://docs.python.org/3/library/copy.html#module-copy) của từ điển `memos`.
2. Nếu tài liệu đã có [trong](https://docs.python.org/3/library/stdtypes.html#dict) từ điển `memos`, chỉ cần `return` số lượng từ tương ứng và bản sao của `memos`. Không cần tính toán lại số lượng từ.
3. Nếu không, sử dụng hàm `word_count` đã được cung cấp để đếm các từ trong `document` đã cho.
4. Lưu trữ số lượng từ vào bản sao của `memos`.
5. `return` số lượng từ và bản sao `memos` đã được cập nhật.

## Khái Niệm Kỹ Thuật Chính

- **Cache Hit**: Khi tài liệu đã có trong từ điển `memos` - trả về ngay lập tức
- **Cache Miss**: Khi tài liệu chưa có - cần tính toán và lưu trữ
- **Memory Trade-off**: Đánh đổi bộ nhớ để tăng tốc độ xử lý
- **Pure Function Memoization**: Chỉ các hàm thuần khiết mới an toàn để ghi nhớ hóa