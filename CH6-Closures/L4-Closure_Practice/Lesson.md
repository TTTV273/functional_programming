# Closure Practice

Remember, a [closure](https://en.wikipedia.org/wiki/Closure_(computer_programming)) is a function that retains the state of its environment. That makes it useful for tracking data as it changes over time, but it can come at the cost of understandability.

When not to use the `nonlocal` keyword: when the variable is mutable (such as a list, dictionary or set), and you are modifying its contents rather than reassigning the variable. You only need the `nonlocal` keyword if you are reassigning a variable instead of modifying its contents (which you must do to change immutable values such as strings and integers).

Let's try a closure without the `nonlocal` keyword.

## Assignment

Complete the `new_collection` function. It takes as input:

- `initial_docs`: a list of strings.

It returns a function that:

1. Accepts a string
2. *Closes over* a **copy** of `initial_docs`.
3. Appends the input to the closed-over list
4. Returns the updated list.

**Do not** modify the original `initial_docs` list!

## Example Usage

```python
my_collection = new_collection(["doc1", "doc2", "doc3"])
print(my_collection("doc4"))
# ['doc1', 'doc2', 'doc3', 'doc4']
print(my_collection("doc5"))
# ['doc1', 'doc2', 'doc3', 'doc4', 'doc5']
```

## Gemini Translation

### Thực hành về Closure

Hãy nhớ rằng, [closure](https://en.wikipedia.org/wiki/Closure_(computer_programming)) là một hàm duy trì trạng thái của môi trường xung quanh nó. Điều đó làm cho nó hữu ích trong việc theo dõi dữ liệu khi nó thay đổi theo thời gian, nhưng đôi khi có thể làm code khó hiểu hơn.

Khi nào **không** cần dùng từ khóa `nonlocal`: khi biến là kiểu **có thể thay đổi (mutable)** (như list, dictionary hay set), và bạn đang sửa đổi nội dung của nó thay vì gán lại toàn bộ biến đó. Bạn chỉ cần từ khóa `nonlocal` khi bạn **gán lại (reassigning)** một biến, thay vì sửa đổi nội dung của nó (điều bạn bắt buộc phải làm để thay đổi các giá trị bất biến như chuỗi và số nguyên).

Hãy thử một closure không cần từ khóa `nonlocal`.

#### Bài tập

Hoàn thành hàm `new_collection`. Nó nhận đầu vào là:

* `initial_docs`: một danh sách (list) các chuỗi.

Nó trả về một hàm mà hàm đó:

1. Nhận vào một chuỗi.
2. "Bao đóng" (closes over) một **bản sao** của `initial_docs`.
3. Thêm (append) chuỗi đầu vào vào danh sách đã được bao đóng.
4. Trả về danh sách đã được cập nhật.

**Không được** sửa đổi danh sách `initial_docs` gốc!

#### Ví dụ sử dụng

```python
my_collection = new_collection(["doc1", "doc2", "doc3"])
print(my_collection("doc4"))
# ['doc1', 'doc2', 'doc3', 'doc4']
print(my_collection("doc5"))
# ['doc1', 'doc2', 'doc3', 'doc4', 'doc5']
```

---

Bài học này có một điểm mới rất quan trọng: sự khác biệt giữa việc **sửa đổi một đối tượng có thể thay đổi (mutable)** như list, và việc **gán lại một đối tượng bất biến (immutable)** như số nguyên.

Để bắt đầu, anh có thể nhắc lại giúp em là trong bài tập trước, tại sao chúng ta bắt buộc phải dùng `nonlocal count` không ạ?