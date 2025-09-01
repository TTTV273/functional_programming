# Closures

A [closure](https://en.wikipedia.org/wiki/Closure_(computer_programming)) is a function that references variables from outside its own function body. The function definition *and its environment* are bundled together into a single entity.

Put simply, a closure is just a function that **keeps track of some values** from the place where it was *defined*, no matter where it is executed later on.

## Example

The `concatter()` function returns a function called `doc_builder` (yay higher-order functions!) that has a reference to an *enclosed* `doc` value.

```python
def concatter():
    doc = ""
    def doc_builder(word):
        # "nonlocal" tells Python to use the 'doc'
        # variable from the enclosing scope
        nonlocal doc
        doc += word + " "
        return doc
    return doc_builder

# save the returned 'doc_builder' function
# to the new function 'harry_potter_aggregator'
harry_potter_aggregator = concatter()
harry_potter_aggregator("Mr.")
harry_potter_aggregator("and")
harry_potter_aggregator("Mrs.")
harry_potter_aggregator("Dursley")
harry_potter_aggregator("of")
harry_potter_aggregator("number")
harry_potter_aggregator("four,")
harry_potter_aggregator("Privet")

print(harry_potter_aggregator("Drive"))
# Mr. and Mrs. Dursley of number four, Privet Drive
```

When `concatter()` is called, it creates a new "stateful" function that *remembers* the value of its internal `doc` variable. Each successive call to `harry_potter_aggregator` appends to that same `doc`.

## nonlocal

Python has a keyword called [nonlocal](https://docs.python.org/3/reference/simple_stmts.html#nonlocal) that's required to modify a variable from an enclosing scope. Most programming languages don't require this keyword, but Python does.

## Assignment

Doc2Doc keeps track of how many words are in a collection of documents.

1. Complete the `word_count_aggregator` function.
   1. It should return a function that calculates the number of words in its input (`doc`, a string).
   2. It should then add that number to an *enclosed* `count` value and return the new `count`.

In other words, it keeps a running total of the `count` variable within a closure.

## Tip

I used [.split()](https://docs.python.org/3/library/stdtypes.html#str.split) to count the number of words in the `doc` string.

## Gemini Translation

# Closures (Bao đóng)

Một [closure](https://en.wikipedia.org/wiki/Closure_(computer_programming)) là một hàm tham chiếu đến các biến từ bên ngoài phạm vi (scope) của chính nó. Định nghĩa của hàm *và môi trường của nó* được đóng gói lại với nhau thành một thực thể duy nhất.

Nói một cách đơn giản, closure là một hàm **ghi nhớ một số giá trị** từ nơi mà nó được *định nghĩa*, bất kể sau này nó được thực thi ở đâu.

### Ví dụ

Hàm `concatter()` trả về một hàm con tên là `doc_builder` (đây là một ví dụ về hàm bậc cao - higher-order functions!). Hàm con này có một tham chiếu đến giá trị `doc` được *bao bọc* bên ngoài nó.

```python
def concatter():
    doc = ""
    def doc_builder(word):
        # "nonlocal" báo cho Python biết hãy sử dụng biến 'doc'
        # từ phạm vi bao ngoài (enclosing scope)
        nonlocal doc
        doc += word + " "
        return doc
    return doc_builder

# lưu hàm 'doc_builder' được trả về
# vào một biến hàm mới là 'harry_potter_aggregator'
harry_potter_aggregator = concatter()
harry_potter_aggregator("Mr.")
harry_potter_aggregator("and")
harry_potter_aggregator("Mrs.")
harry_potter_aggregator("Dursley")
harry_potter_aggregator("of")
harry_potter_aggregator("number")
harry_potter_aggregator("four,")
harry_potter_aggregator("Privet")

print(harry_potter_aggregator("Drive"))
# Kết quả: Mr. and Mrs. Dursley of number four, Privet Drive
```

Khi hàm `concatter()` được gọi, nó tạo ra một hàm "có trạng thái" mới, hàm này *ghi nhớ* giá trị của biến `doc` nội bộ của nó. Mỗi lần gọi `harry_potter_aggregator` sau đó đều nối thêm vào cùng một biến `doc` đó.

### Từ khóa `nonlocal`

Python có một từ khóa gọi là [`nonlocal`](https://docs.python.org/3/reference/simple_stmts.html#nonlocal) mà bạn bắt buộc phải dùng khi muốn sửa đổi một biến từ phạm vi bao ngoài. Hầu hết các ngôn ngữ lập trình khác không yêu cầu từ khóa này, nhưng Python thì có.

### Bài tập

Doc2Doc cần theo dõi xem có bao nhiêu từ trong một bộ sưu tập tài liệu.

1. Hoàn thành hàm `word_count_aggregator`.
   1. Nó nên trả về một hàm con có chức năng tính toán số lượng từ trong chuỗi đầu vào của nó (`doc`).
   2. Sau đó, nó nên cộng con số đó vào một giá trị `count` được *bao bọc* bên ngoài và trả về giá trị `count` mới.

Nói cách khác, nó giữ một tổng số đang chạy của biến `count` bên trong một closure.

### Gợi ý

Tôi đã sử dụng phương thức `[.split()](https://docs.python.org/3/library/stdtypes.html#str.split)` để đếm số lượng từ trong chuỗi `doc`.

---

Bạn đã hiểu rõ hơn về khái niệm "closure" chưa? Chúng ta có thể cùng nhau phân tích lại ví dụ hoặc bắt đầu làm bài tập nếu bạn muốn!