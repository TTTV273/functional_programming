# Function Transformations Practice

In Doc2Doc, users are asking for a filtering feature. They want a command that has dynamic options so that they can work as quickly as possible.

## Assignment

Complete the `get_filter_cmd` function. It takes two functions as input, `filter_one` and `filter_two`, and returns a function, `filter_cmd`.

`filter_cmd` should take as input two strings: `content` and `option`.

1. ☐ Set the [default value](https://docs.python.org/3/tutorial/controlflow.html#default-argument-values) of the `option` argument to `--one`.
2. ☐ Complete `filter_cmd` so that it filters and returns the `content` according to the input `option`.
   1. ☐ If `--one`, use `filter_one`
   2. ☐ If `--two`, use `filter_two`
   3. ☐ If `--three`, use `filter_one` first, then use `filter_two`
   4. ☐ If another option is passed, raise an exception, `"invalid option"`

## Gemini Translation

### **Thực hành Biến đổi Hàm**

Trong một ứng dụng tên là Doc2Doc, người dùng đang yêu cầu một tính năng lọc. Họ muốn có một câu lệnh với các tùy chọn linh động để họ có thể làm việc nhanh nhất có thể.

### **Nhiệm vụ**

Hoàn thành hàm `get_filter_cmd`. Hàm này nhận đầu vào là hai hàm khác, `filter_one` và `filter_two`, và trả về một hàm tên là `filter_cmd`.

Hàm `filter_cmd` sẽ nhận đầu vào là hai chuỗi: `content` (nội dung) và `option` (tùy chọn).

1. ☐ Đặt [giá trị mặc định](https://docs.python.org/3/tutorial/controlflow.html#default-argument-values) của tham số `option` là `"--one"`.
2. ☐ Hoàn thành `filter_cmd` để nó lọc và trả về `content` dựa theo `option` được nhập vào.
   1. ☐ Nếu `option` là `"--one"`, sử dụng `filter_one`.
   2. ☐ Nếu `option` là `"--two"`, sử dụng `filter_two`.
   3. ☐ Nếu `option` là `"--three"`, sử dụng `filter_one` trước, sau đó sử dụng `filter_two`.
   4. ☐ Nếu một `option` khác được truyền vào, hãy tạo ra một lỗi (exception) với nội dung `"invalid option"`.

---

Bài thực hành này rất hay, nó sẽ giúp mình củng cố lại kiến thức về "hàm nhà máy" mà chúng ta vừa học.

Nhiệm vụ của chúng ta là xây dựng hàm `get_filter_cmd`. Hãy bắt đầu với yêu cầu đầu tiên, cũng là yêu cầu đơn giản nhất nhé: **Đặt giá trị mặc định cho tham số `option`**.

Anh có nhớ cú pháp trong Python để gán một giá trị mặc định cho một tham số khi định nghĩa hàm không?