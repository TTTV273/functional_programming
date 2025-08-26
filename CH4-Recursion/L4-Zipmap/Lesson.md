# Zipmap

Let's practice another simple recursive function.

You may not understand recursion just yet, but by following the instructions, you will begin to grasp the fundamentals.

## Assignment

Within Doc2Doc we need to map certain properties from one document to properties of another document. Complete the recursive `zipmap` function.

It takes two lists as input and returns a [dictionary](https://docs.python.org/3/tutorial/datastructures.html#dictionaries) where the first list provides the *keys* and the second list provides the *values*.

Example usage:

```python
zipped = zipmap(
    ["Avatar: The Last Airbender", "Avatar (in Papyrus font)", "The Last Airbender (Live Action)"],
    [9.9, 6.1, 2.1]
)

print(zipped)
# {
#   'Avatar: The Last Airbender': 9.9,
#   'Avatar (in Papyrus font)': 6.1,
#   'The Last Airbender (Live Action)': 2.1,
# }
```

Here's the [pseudocode](https://en.wikipedia.org/wiki/Pseudocode):

1. If either the `keys` or `values` list is empty, return an empty dictionary (base case). This takes care of creating a dictionary.
2. Recursively call `zipmap` on all but the first elements from `keys` and `values`
3. Add the first element of `keys` to the resulting dictionary, and set its value to the first element in `values`
4. Return the updated dictionary

---

## Gemini Translation

**Zipmap**

Nào, hãy cùng thực hành một hàm đệ quy đơn giản khác.

Có thể anh vẫn chưa hiểu hoàn toàn về đệ quy, nhưng bằng cách làm theo hướng dẫn, anh sẽ bắt đầu nắm bắt được những điều cơ bản.

## Bài tập

Trong Doc2Doc, chúng ta cần ánh xạ (map) các thuộc tính nhất định từ một tài liệu sang các thuộc tính của một tài liệu khác. Anh hãy hoàn thành hàm đệ quy `zipmap`.

Hàm này nhận hai danh sách (list) làm đầu vào và trả về một **từ điển (dictionary)**, trong đó danh sách đầu tiên cung cấp các **khóa (keys)** và danh sách thứ hai cung cấp các **giá trị (values)**.

Ví dụ sử dụng:

```python
zipped = zipmap(
    ["Avatar: The Last Airbender", "Avatar (in Papyrus font)", "The Last Airbender (Live Action)"],
    [9.9, 6.1, 2.1]
)

print(zipped)
# Kết quả:
# {
#   'Avatar: The Last Airbender': 9.9,
#   'Avatar (in Papyrus font)': 6.1,
#   'The Last Airbender (Live Action)': 2.1,
# }
```

Đây là **mã giả (pseudocode)** để thực hiện:

1. Nếu một trong hai danh sách `keys` hoặc `values` bị rỗng, hãy trả về một từ điển rỗng (đây là **trường hợp cơ sở**). Bước này đảm nhiệm việc tạo ra một từ điển.
2. Gọi đệ quy hàm `zipmap` với phần còn lại của danh sách `keys` và `values` (tức là bỏ đi phần tử đầu tiên của mỗi danh sách).
3. Thêm phần tử đầu tiên của `keys` vào từ điển kết quả (nhận được từ bước 2), và gán giá trị cho nó là phần tử đầu tiên trong `values`.
4. Trả về từ điển đã được cập nhật.

Bài học này cung cấp các bước hướng dẫn rất chi tiết. Trước khi mình xem các tệp code, anh nghĩ mình sẽ viết **trường hợp cơ sở** (bước 1 trong mã giả) trong Python như thế nào?